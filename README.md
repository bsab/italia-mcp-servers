<p align="center">
  <img src="logo.svg" alt="italia MCP servers" width="700"/>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"/></a>
  <img src="https://img.shields.io/badge/server%20MCP-23-blue.svg" alt="23 server"/>
  <img src="https://img.shields.io/badge/categorie-6-orange.svg" alt="6 categorie"/>
  <img src="https://img.shields.io/badge/made%20in-Italy%20%F0%9F%87%AE%F0%9F%87%B9-red.svg" alt="Made in Italy"/>
</p>

---

**Catalogo curato dei server [MCP](https://modelcontextprotocol.io/) (Model Context Protocol) italiani**: dati pubblici, legal-tech, fatturazione elettronica, pubblica amministrazione e altro.

Il Model Context Protocol permette agli assistenti AI (Claude, Cursor, VS Code Copilot...) di collegarsi a fonti dati e strumenti esterni in modo standardizzato. Questo catalogo raccoglie tutti i server MCP sviluppati per il contesto italiano.

## 📊 Dati e Statistiche

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**ISTAT MCP Server**](https://github.com/ondata/istat_mcp_server) | 23 | Python | Statistiche ISTAT via SDMX API — il più maturo |
| [ISTAT MCP](https://github.com/SimonBerg255/istat-mcp) | 3 | Python | 4700+ dataset ISTAT via SDMX, senza API key |
| [ISTAT MCP Suite](https://github.com/ManoloZocco/istat-mcp-suite) | 0 | Python | Server unificato per dataset ISTAT |
| [OpenData AI](https://github.com/agent-engineering-studio/opendata-ai) | 1 | Python | Multi-source: CKAN, ISTAT, Eurostat, OECD |

## ⚖️ Legal-Tech e Normativa

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**BetterCallClaude Italia**](https://github.com/fedec65/bettercallclaude_italia) | 44 | JS | Quadro normativo italiano completo |
| [**MCP Legal IT**](https://github.com/capazme/mcp-legal-it) | 14 | Python | 200+ tool: statuti, giurisprudenza, calcoli legali |
| [Gov IT Legal MCP](https://github.com/SimonBerg255/gov-it-legal-mcp) | 10 | Python | Normattiva + sentenze TAR/CdS |
| [AnonyMCP](https://github.com/avvocati-e-mac/AnonyMCP) | 5 | TS | Pseudonimizza documenti legali prima dell'LLM |
| [Italian Law MCP](https://github.com/Ansvar-Systems/italian-law-mcp) | 1 | TS | GDPR, Codice Privacy, cybercrime |
| [Normattiva MCP](https://github.com/adellorto/normattiva-mcp) | 1 | Python | API di Normattiva |
| [Normattiva MCP (CLI)](https://github.com/avvocati-e-mac/normattiva-mcp) | 0 | Python | CLI + MCP per citare norme da Normattiva.it |

## 🧾 Fatturazione Elettronica

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**Fatture in Cloud MCP**](https://github.com/aringad/fattureincloud-mcp) | 18 | Python | Fatture in Cloud API con Claude AI |
| [Aruba Fatture MCP](https://github.com/MarckDev/aruba-fatture-mcp) | 3 | TS | Aruba Fatturazione Elettronica + SDI |
| [FattureInCloudMCP](https://github.com/badbat75/FattureInCloudMCP) | 0 | TS | Fatture in Cloud API v2, CRUD completo |

## 🏛️ PA, Parlamento e Finanza Pubblica

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**DoveVannoINostriSoldi**](https://github.com/Italian-Builders-Org/DoveVannoINostriSoldi) | 258 | TS | Spesa pubblica: SIOPE, debito, PNRR, IRPEF e altro — [endpoint remoto](https://www.dovevannoinostrisoldi.com/api/mcp) |
| [Cruscotto Italia MCP](https://cruscotto-italia-mcp.agid.workers.dev/mcp) | 0 | TS | Dati comunali per codice ISTAT: demografia, SIOPE, PNRR, sanità |
| [**Dichiarino MCP**](https://github.com/gsaccardi/dichiarino-mcp) | 23 | Python | Assistente per la dichiarazione dei redditi |
| [ANAC MCP](https://github.com/SimonBerg255/anac-mcp) | 4 | Python | Appalti pubblici ANAC (BDNCP) |
| [Italian Parliament MCP](https://github.com/ondata/italianparliament-mcp) | 2 | TS | Dati del Parlamento italiano |

## 🛡️ Cybersecurity e Compliance

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [Italian Cybersecurity MCP](https://github.com/Ansvar-Systems/italian-cybersecurity-mcp) | 0 | TS | ACN — linee guida e advisory |
| [Italian Competition MCP](https://github.com/Ansvar-Systems/italian-competition-mcp) | 0 | TS | AGCM — decisioni antitrust |

## 🎨 Design e Altro

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [Filo — Design System Italia](https://github.com/Fupete/design-system-italia-mcp) | 3 | TS | Design system .italia (sperimentale) |
| [MCP Meteo Italia](https://github.com/makremriahi99/MCP-Meteo-Italia) | 0 | Python | Meteo in tempo reale con FastMCP + Gradio |

---

## 📈 Statistiche

| Metrica | Valore |
|---------|--------|
| Server totali | **23** |
| Python | 12 |
| TypeScript | 9 |
| JavaScript | 2 |
| Licenze open source | 18 |
| Categorie | 6 |

## 🤝 Come contribuire

Conosci un server MCP italiano non presente in questo catalogo? Apri una PR!

1. Crea un file JSON in `servers/` con il nome in `kebab-case.json`
2. Segui lo schema:

```json
{
  "name": "Nome del Server",
  "repository_url": "https://github.com/owner/repo",
  "site_url": "https://...",
  "author": "owner",
  "language": "Python",
  "license": "MIT",
  "stars": 0,
  "category": "dati-statistiche",
  "description": "Breve descrizione del server (max 200 caratteri).",
  "tags": ["tag1", "tag2", "tag3"]
}
```

### Categorie ammesse

| Categoria | Descrizione |
|-----------|-------------|
| `dati-statistiche` | ISTAT, Eurostat, open data |
| `legal-tech` | Normativa, giurisprudenza, privacy |
| `fatturazione` | Fatture elettroniche, SDI |
| `pa-finanza-pubblica` | PA, parlamento, fisco, appalti |
| `cybersecurity-compliance` | ACN, AGCM, compliance |
| `design-altro` | Design system, meteo, altro |

### Criteri di inclusione

- Il server deve implementare il **Model Context Protocol**
- Deve essere **pertinente al contesto italiano** (dati, normativa, servizi italiani)
- Il repository deve essere **pubblico** su GitHub
- Deve avere un README con istruzioni di utilizzo

## 📜 Licenza

Questo catalogo è distribuito sotto licenza [MIT](LICENSE).

I singoli server elencati sono sotto le rispettive licenze indicate.

---

<p align="center">
  <i>Fatto con ❤️ in Italia — per rendere i dati italiani accessibili all'AI</i>
</p>