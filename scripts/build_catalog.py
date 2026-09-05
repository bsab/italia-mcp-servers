#!/usr/bin/env python3
"""Costruisce il sito statico pubblicato su GitHub Pages.

Genera in site/:
  - catalog.json                 catalogo aggregato, leggibile dalle macchine
  - schema/server.schema.json    copia dello schema, referenziata da catalog.json
  - index.html                   pagina di consultazione con ricerca e filtri

Uso:
    python3 scripts/build_catalog.py [--output site]
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_readme import CATEGORIES, load_servers, primary_url, sort_key  # noqa: E402
from quality import quality_rubric, readiness_score  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
SERVER_SCHEMA = SCHEMA_DIR / "server.schema.json"
CATALOG_SCHEMA = SCHEMA_DIR / "catalog.schema.json"
TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "index.html"

BASE_URL = "https://bsab.github.io/italia-mcp-servers"

# Versione della struttura di catalog.json. Va incrementata a ogni modifica
# incompatibile, perche' l'URL pubblico e' a tutti gli effetti un'API.
CATALOG_VERSION = 1


def build_catalog(servers: list[dict]) -> dict:
    by_category = {category.slug: 0 for category in CATEGORIES}
    for server in servers:
        by_category[server["category"]] += 1

    entries = []
    for server in sorted(servers, key=sort_key):
        entry = {key: value for key, value in server.items() if not key.startswith("_")}
        entry["url"] = primary_url(server)
        entry["readiness_score"] = readiness_score(server)
        entries.append(entry)

    return {
        "$schema": f"{BASE_URL}/schema/catalog.schema.json",
        "version": CATALOG_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "https://github.com/bsab/italia-mcp-servers",
        "license": "MIT",
        "quality_rubric": quality_rubric(),
        "count": len(entries),
        "categories": [
            {
                "id": category.slug,
                "label": category.label,
                "emoji": category.emoji,
                "description": category.description,
                "count": by_category[category.slug],
            }
            for category in CATEGORIES
        ],
        "servers": entries,
    }


def validate_catalog(catalog: dict) -> None:
    """Valida il catalogo generato, se jsonschema e' disponibile.

    Il cross-reference tra i due schemi va registrato esplicitamente, perche'
    catalog.schema.json referenzia server.schema.json per URL e non lo scarica.
    """
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from referencing import Registry, Resource
    except ImportError:
        print(
            "jsonschema non installato: catalog.json non e' stato validato "
            "(python3 -m pip install -r scripts/requirements.txt)",
            file=sys.stderr,
        )
        return

    server_schema = json.loads(SERVER_SCHEMA.read_text(encoding="utf-8"))
    catalog_schema = json.loads(CATALOG_SCHEMA.read_text(encoding="utf-8"))
    registry = Registry().with_resource(
        uri=server_schema["$id"], resource=Resource.from_contents(server_schema)
    )

    validator = Draft202012Validator(
        catalog_schema, registry=registry, format_checker=FormatChecker()
    )
    errors = sorted(validator.iter_errors(catalog), key=lambda e: list(e.absolute_path))
    if errors:
        for error in errors:
            location = "".join(f"[{part!r}]" for part in error.absolute_path)
            print(f"catalog.json: {location or '<root>'}: {error.message}", file=sys.stderr)
        sys.exit(f"\n{len(errors)} errori nel catalogo generato.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default="site",
        help="directory di destinazione (default: site)",
    )
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output

    servers = load_servers()
    catalog = build_catalog(servers)
    validate_catalog(catalog)

    if output.exists():
        shutil.rmtree(output)
    (output / "schema").mkdir(parents=True)

    (output / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    shutil.copyfile(SERVER_SCHEMA, output / "schema" / "server.schema.json")
    shutil.copyfile(CATALOG_SCHEMA, output / "schema" / "catalog.schema.json")
    (output / "index.html").write_text(
        TEMPLATE_PATH.read_text(encoding="utf-8"), encoding="utf-8"
    )
    # Evita che GitHub Pages processi i file con Jekyll.
    (output / ".nojekyll").write_text("", encoding="utf-8")

    print(f"{output.name}/ generato: {catalog['count']} server, versione {CATALOG_VERSION}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
