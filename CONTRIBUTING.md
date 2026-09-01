# Come contribuire a italia-mcp-servers

## Aggiungere un server MCP

1. **Fai un fork** del repository
2. Crea un file JSON in `servers/` con nome in `kebab-case.json`
3. Compila tutti i campi richiesti (vedi schema nel README)
4. Rigenera il README con `python3 scripts/build_readme.py` e includi il file aggiornato nel commit
5. Apri una Pull Request con titolo: `feat: added Nome Server`

> Le tabelle del catalogo, i badge e le statistiche nel README sono generati
> automaticamente dai file in `servers/`: non modificarli a mano, altrimenti le
> modifiche vengono sovrascritte alla rigenerazione successiva.

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