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

> Le tabelle del catalogo, i badge e le statistiche nel README sono generati
> automaticamente dai file in `servers/`: non modificarli a mano, altrimenti le
> modifiche vengono sovrascritte alla rigenerazione successiva.

## Script di manutenzione

| Comando | Cosa fa |
|---------|---------|
| `python3 scripts/validate_servers.py` | Valida `servers/` contro lo schema e controlla nomi di file, duplicati e URL |
| `python3 scripts/build_readme.py` | Rigenera badge, tabelle e statistiche del README |
| `python3 scripts/build_readme.py --check` | Verifica l'allineamento senza riscrivere nulla (usato dalla CI) |

## Criteri

- Il server deve implementare il Model Context Protocol
- Deve essere pertinente al contesto italiano
- Il repository deve essere pubblico su GitHub
- Deve avere documentazione d'uso

## Segnalare problemi

- Link non funzionanti
- Informazioni errate o obsolete
- Server non più mantenuti

Apri una [issue](https://github.com/bsab/italia-mcp-servers/issues) con i dettagli.