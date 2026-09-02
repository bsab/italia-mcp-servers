#!/usr/bin/env python3
"""Rigenera le sezioni dinamiche del README a partire dai file in servers/.

Uso:
    python3 scripts/build_readme.py            # riscrive il README
    python3 scripts/build_readme.py --check    # esce con 1 se il README non e' aggiornato
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
SERVERS_DIR = ROOT / "servers"
README = ROOT / "README.md"


class Category(NamedTuple):
    slug: str
    emoji: str
    label: str
    description: str

    @property
    def heading(self) -> str:
        return f"{self.emoji} {self.label}"


# Categorie ammesse, nell'ordine in cui compaiono nel README.
# L'emoji e' separata dalla label perche' serve solo alle intestazioni Markdown:
# i consumatori di catalog.json ricevono la label pulita.
CATEGORIES = [
    Category("dati-statistiche", "📊", "Dati e Statistiche", "ISTAT, Eurostat, open data"),
    Category("legal-tech", "⚖️", "Legal-Tech e Normativa", "Normativa, giurisprudenza, privacy"),
    Category("fatturazione", "🧾", "Fatturazione Elettronica", "Fatture elettroniche, SDI"),
    Category("pa-finanza-pubblica", "🏛️", "PA, Parlamento e Finanza Pubblica", "PA, parlamento, fisco, appalti"),
    Category("cybersecurity-compliance", "🛡️", "Cybersecurity e Compliance", "ACN, AGCM, compliance"),
    Category("design-altro", "🎨", "Design e Altro", "Design system, meteo, altro"),
]

# Abbreviazioni usate nella colonna "Lang" del catalogo.
LANGUAGE_ABBR = {"TypeScript": "TS", "JavaScript": "JS"}

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


def render_row(server: dict) -> str:
    name = html.escape(server["name"])
    label = f"<strong>{name}</strong>" if server.get("featured") else name
    url = html.escape(primary_url(server), quote=True)
    description = html.escape(server.get("short_description") or server["description"])
    endpoint = server.get("mcp_endpoint")
    language = server.get("language", "—")
    connect = "—"
    if endpoint:
        escaped_endpoint = html.escape(endpoint, quote=True)
        connect = (
            f'<a href="{escaped_endpoint}" target="_blank" rel="noopener noreferrer" '
            f'title="Apri endpoint MCP: {name}"><kbd>Connetti</kbd></a>'
        )

    return (
        "  <tr>\n"
        f'    <td><a href="{url}">{label}</a></td>\n'
        f'    <td align="right">{server.get("stars", 0)}</td>\n'
        f"    <td>{html.escape(LANGUAGE_ABBR.get(language, language))}</td>\n"
        f"    <td>{description}</td>\n"
        f"    <td align=\"center\">{connect}</td>\n"
        "  </tr>"
    )


def render_catalog(servers: list[dict]) -> str:
    known = {category.slug for category in CATEGORIES}
    for server in servers:
        if server.get("category") not in known:
            sys.exit(f"{server['_path']}: categoria sconosciuta {server.get('category')!r}")

    sections = []
    for category in CATEGORIES:
        rows = sorted((s for s in servers if s["category"] == category.slug), key=sort_key)
        if not rows:
            continue
        body = "\n".join(render_row(server) for server in rows)
        sections.append(
            f"### {category.heading}\n\n"
            '<table width="100%">\n'
            "  <thead>\n"
            "    <tr>\n"
            '      <th width="24%">Progetto</th>\n'
            '      <th width="8%" align="right">⭐</th>\n'
            '      <th width="10%">Lang</th>\n'
            '      <th width="46%">Descrizione</th>\n'
            '      <th width="12%">Link</th>\n'
            "    </tr>\n"
            "  </thead>\n"
            "  <tbody>\n"
            f"{body}\n"
            "  </tbody>\n"
            "</table>"
        )
    return "\n\n".join(sections)


def render_badges(servers: list[dict]) -> str:
    categories = len({s["category"] for s in servers})
    return (
        '  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/ci.yml">'
        '<img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/ci.yml/badge.svg" '
        'alt="CI"/></a>\n'
        '  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/link-check.yml">'
        '<img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/link-check.yml/badge.svg" '
        'alt="Link check"/></a>\n'
        '  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/pages.yml">'
        '<img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/pages.yml/badge.svg" '
        'alt="GitHub Pages"/></a>\n'
        '  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" '
        'alt="MIT License"/></a>\n'
        f'  <img src="https://img.shields.io/badge/server%20MCP-{len(servers)}-blue.svg" '
        f'alt="{len(servers)} server"/>\n'
        f'  <img src="https://img.shields.io/badge/categorie-{categories}-orange.svg" '
        f'alt="{categories} categorie"/>'
    )


def replace_block(content: str, name: str, body: str) -> str:
    pattern = re.compile(BLOCK_RE_TEMPLATE.format(name=re.escape(name)), re.S)
    if not pattern.search(content):
        sys.exit(f"README.md: marker <!-- BEGIN:{name} --> / <!-- END:{name} --> non trovato")
    # Il body e' inserito tramite lambda per evitare che \g, \1 ecc. vengano interpretati.
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), content)


def build(content: str, servers: list[dict]) -> str:
    content = replace_block(content, "badges", render_badges(servers))
    content = replace_block(content, "catalog", render_catalog(servers))
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
