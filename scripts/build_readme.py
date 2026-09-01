#!/usr/bin/env python3
"""Rigenera le sezioni dinamiche del README a partire dai file in servers/.

Uso:
    python3 scripts/build_readme.py            # riscrive il README
    python3 scripts/build_readme.py --check    # esce con 1 se il README non e' aggiornato
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVERS_DIR = ROOT / "servers"
README = ROOT / "README.md"

# Ordine, intestazione e descrizione delle categorie ammesse.
CATEGORIES = [
    ("dati-statistiche", "📊 Dati e Statistiche", "ISTAT, Eurostat, open data"),
    ("legal-tech", "⚖️ Legal-Tech e Normativa", "Normativa, giurisprudenza, privacy"),
    ("fatturazione", "🧾 Fatturazione Elettronica", "Fatture elettroniche, SDI"),
    ("pa-finanza-pubblica", "🏛️ PA, Parlamento e Finanza Pubblica", "PA, parlamento, fisco, appalti"),
    ("cybersecurity-compliance", "🛡️ Cybersecurity e Compliance", "ACN, AGCM, compliance"),
    ("design-altro", "🎨 Design e Altro", "Design system, meteo, altro"),
]

# Abbreviazioni usate nella colonna "Lang" del catalogo.
LANGUAGE_ABBR = {"TypeScript": "TS", "JavaScript": "JS"}

# Valori di `license` che non identificano una licenza open source riconosciuta.
NON_OSS_LICENSES = {"n/a", "unknown", "noassertion", ""}

BLOCK_RE_TEMPLATE = r"(<!-- BEGIN:{name} -->\n)(?:.*?)(\n<!-- END:{name} -->)"


def load_servers() -> list[dict]:
    servers = []
    for path in sorted(SERVERS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            try:
                data = json.load(fh)
            except json.JSONDecodeError as exc:
                sys.exit(f"{path}: JSON non valido: {exc}")
        data["_path"] = path
        servers.append(data)
    if not servers:
        sys.exit(f"{SERVERS_DIR}: nessun server trovato")
    return servers


def primary_url(server: dict) -> str:
    for key in ("repository_url", "site_url", "mcp_endpoint"):
        url = server.get(key)
        if url:
            return url
    sys.exit(f"{server['_path']}: manca un URL (repository_url, site_url o mcp_endpoint)")


def sort_key(server: dict):
    return (not server.get("featured", False), -server.get("stars", 0), server["name"].lower())


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_row(server: dict) -> str:
    name = escape_cell(server["name"])
    label = f"**{name}**" if server.get("featured") else name
    url = primary_url(server)
    description = escape_cell(server.get("short_description") or server["description"])

    endpoint = server.get("mcp_endpoint")
    if endpoint and endpoint != url:
        description += f" — [endpoint remoto]({endpoint})"

    language = server.get("language", "—")
    return (
        f"| [{label}]({url}) | {server.get('stars', 0)} | "
        f"{escape_cell(LANGUAGE_ABBR.get(language, language))} | {description} |"
    )


def render_catalog(servers: list[dict]) -> str:
    known = {slug for slug, _, _ in CATEGORIES}
    for server in servers:
        if server.get("category") not in known:
            sys.exit(f"{server['_path']}: categoria sconosciuta {server.get('category')!r}")

    sections = []
    for slug, title, _ in CATEGORIES:
        rows = sorted((s for s in servers if s["category"] == slug), key=sort_key)
        if not rows:
            continue
        body = "\n".join(render_row(server) for server in rows)
        sections.append(
            f"## {title}\n\n"
            "| Progetto | ⭐ | Lang | Descrizione |\n"
            "|----------|---:|------|-------------|\n"
            f"{body}"
        )
    return "\n\n".join(sections)


def render_stats(servers: list[dict]) -> str:
    languages: dict[str, int] = {}
    for server in servers:
        language = server.get("language", "—")
        languages[language] = languages.get(language, 0) + 1

    oss = sum(
        1
        for server in servers
        if str(server.get("license") or "").strip().lower() not in NON_OSS_LICENSES
    )

    lines = [
        "| Metrica | Valore |",
        "|---------|--------|",
        f"| Server totali | **{len(servers)}** |",
    ]
    for language, count in sorted(languages.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {language} | {count} |")
    lines.append(f"| Licenze open source | {oss} |")
    lines.append(f"| Categorie | {len({s['category'] for s in servers})} |")
    return "\n".join(lines)


def render_badges(servers: list[dict]) -> str:
    categories = len({s["category"] for s in servers})
    return (
        '  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" '
        'alt="MIT License"/></a>\n'
        f'  <img src="https://img.shields.io/badge/server%20MCP-{len(servers)}-blue.svg" '
        f'alt="{len(servers)} server"/>\n'
        f'  <img src="https://img.shields.io/badge/categorie-{categories}-orange.svg" '
        f'alt="{categories} categorie"/>\n'
        '  <img src="https://img.shields.io/badge/made%20in-Italy%20%F0%9F%87%AE%F0%9F%87%B9-red.svg" '
        'alt="Made in Italy"/>'
    )


def render_category_table() -> str:
    lines = ["| Categoria | Descrizione |", "|-----------|-------------|"]
    for slug, _, description in CATEGORIES:
        lines.append(f"| `{slug}` | {description} |")
    return "\n".join(lines)


def replace_block(content: str, name: str, body: str) -> str:
    pattern = re.compile(BLOCK_RE_TEMPLATE.format(name=re.escape(name)), re.S)
    if not pattern.search(content):
        sys.exit(f"README.md: marker <!-- BEGIN:{name} --> / <!-- END:{name} --> non trovato")
    # Il body e' inserito tramite lambda per evitare che \g, \1 ecc. vengano interpretati.
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), content)


def build(content: str, servers: list[dict]) -> str:
    content = replace_block(content, "badges", render_badges(servers))
    content = replace_block(content, "catalog", render_catalog(servers))
    content = replace_block(content, "stats", render_stats(servers))
    content = replace_block(content, "categories", render_category_table())
    return content


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verifica che il README sia allineato ai file in servers/ senza riscriverlo",
    )
    args = parser.parse_args()

    servers = load_servers()
    current = README.read_text(encoding="utf-8")
    updated = build(current, servers)

    if args.check:
        if current != updated:
            print(
                "README.md non è aggiornato. Esegui: python3 scripts/build_readme.py",
                file=sys.stderr,
            )
            return 1
        print(f"README.md allineato ({len(servers)} server).")
        return 0

    if current == updated:
        print(f"README.md già aggiornato ({len(servers)} server).")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"README.md rigenerato ({len(servers)} server).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
