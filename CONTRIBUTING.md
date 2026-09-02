# Come contribuire a italia-mcp-servers

## Aggiungere un server MCP

1. **Fai un fork** del repository
2. Crea un file JSON in `servers/` con nome in `kebab-case.json`
3. Compila i campi richiesti da [`schema/server.schema.json`](schema/server.schema.json)
4. Valida e rigenera il README, includendo il file aggiornato nel commit:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_servers.py
python3 scripts/build_readme.py
```

5. Apri una Pull Request con titolo: `feat: added Nome Server`

> Le tabelle del catalogo e i badge nel README sono generati
> automaticamente dai file in `servers/`: non modificarli a mano, altrimenti le
> modifiche vengono sovrascritte alla rigenerazione successiva.

## Script di manutenzione

| Comando | Cosa fa |
|---------|---------|
| `python3 scripts/validate_servers.py` | Valida `servers/` contro lo schema e controlla nomi di file, duplicati e URL |
| `python3 scripts/build_readme.py` | Rigenera badge e tabelle del README |
| `python3 scripts/build_readme.py --check` | Verifica l'allineamento senza riscrivere nulla (usato dalla CI) |
| `python3 scripts/build_catalog.py` | Genera `site/` con `catalog.json` e la pagina di consultazione |

## Catalogo in formato JSON

Il catalogo è pubblicato anche in forma leggibile dalle macchine, rigenerato a ogni
push su `main`:

| Risorsa | URL |
|---------|-----|
| Catalogo | <https://bsab.github.io/italia-mcp-servers/catalog.json> |
| Schema del catalogo | <https://bsab.github.io/italia-mcp-servers/schema/catalog.schema.json> |
| Schema di un server | <https://bsab.github.io/italia-mcp-servers/schema/server.schema.json> |
| Pagina di consultazione | <https://bsab.github.io/italia-mcp-servers/> |

Il campo `version` indica la versione della struttura del documento e cambia solo
per modifiche incompatibili. Ogni voce di `servers` contiene i campi del file
corrispondente più `url`, il link canonico (`repository_url`, altrimenti
`site_url`, altrimenti `mcp_endpoint`).

## Criteri

- Il server deve implementare il Model Context Protocol
- Deve essere pertinente al contesto italiano
- Deve fornire almeno un riferimento pubblico tra repository, sito o endpoint MCP
- Deve avere documentazione d'uso sufficiente

## Segnalare problemi

- Link non funzionanti
- Informazioni errate o obsolete
- Server non più mantenuti

Apri una [issue](https://github.com/bsab/italia-mcp-servers/issues) con i dettagli.