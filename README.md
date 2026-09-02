# Italia MCP Servers 🇮🇹

<p align="center">
  <img src="logo.svg" alt="Logo Italia MCP Servers" width="560"/>
</p>

> Catalogo curato di server [Model Context Protocol](https://modelcontextprotocol.io/)
> dedicati a dati, norme e servizi italiani.

<p align="center">
<!-- BEGIN:badges -->
  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/ci.yml"><img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/link-check.yml"><img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/link-check.yml/badge.svg" alt="Link check"/></a>
  <a href="https://github.com/bsab/italia-mcp-servers/actions/workflows/pages.yml"><img src="https://github.com/bsab/italia-mcp-servers/actions/workflows/pages.yml/badge.svg" alt="GitHub Pages"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"/></a>
  <img src="https://img.shields.io/badge/server%20MCP-31-blue.svg" alt="31 server"/>
  <img src="https://img.shields.io/badge/categorie-6-orange.svg" alt="6 categorie"/>
<!-- END:badges -->
</p>

[Esplora il catalogo](https://bsab.github.io/italia-mcp-servers/) ·
[Consulta l'API JSON](https://bsab.github.io/italia-mcp-servers/catalog.json) ·
[Proponi un server](https://github.com/bsab/italia-mcp-servers/issues/new?template=nuovo-server.yml) ·
[Contribuisci](CONTRIBUTING.md)

## Cos'è questo repository

Il **Model Context Protocol (MCP)** permette ad assistenti AI come GitHub Copilot,
Claude e Cursor di collegarsi a fonti dati e strumenti esterni attraverso
un'interfaccia standard.

Questo repository **non è un singolo server MCP**: è un catalogo pubblico di
progetti pertinenti al contesto italiano, tra cui dati ISTAT e open data,
normativa e giurisprudenza, fatturazione elettronica, pubblica amministrazione,
cybersecurity e design system.

## Inizia qui

| Se vuoi… | Vai a… |
|----------|--------|
| Cercare un server per categoria | [Catalogo web](https://bsab.github.io/italia-mcp-servers/) |
| Integrare il catalogo in un'applicazione | [API JSON](https://bsab.github.io/italia-mcp-servers/catalog.json) |
| Segnalare un progetto mancante | [Proponi un server](https://github.com/bsab/italia-mcp-servers/issues/new?template=nuovo-server.yml) |
| Correggere informazioni errate | [Apri una segnalazione](https://github.com/bsab/italia-mcp-servers/issues/new?template=segnalazione.yml) |
| Aggiungere direttamente un server | [Guida alla contribuzione](CONTRIBUTING.md) |

### Come scegliere e usare un server

1. Scegli una categoria e apri il progetto dalla tabella.
2. Controlla nel README del progetto requisiti, licenza e strumenti disponibili.
3. Se è presente un **endpoint remoto**, collegalo da un client compatibile con
   il transport indicato.
4. Altrimenti installa il server localmente e aggiungi il comando di avvio alla
   configurazione del tuo client MCP.

> La configurazione varia tra client e server. Questo catalogo raccoglie i
> riferimenti; le istruzioni operative ufficiali restano quelle del singolo progetto.

## Catalogo

I progetti in **grassetto** sono messi in evidenza dai manutentori. Le stelle
sono una fotografia indicativa e non rappresentano una valutazione di qualità.

<!-- BEGIN:catalog -->
### 📊 Dati e Statistiche

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**CKAN MCP Server**](https://github.com/ondata/ckan-mcp-server) | 57 | TS | Connettore generico per istanze CKAN (dati.gov.it e portali regionali) |
| [**ISTAT MCP Server**](https://github.com/ondata/istat_mcp_server) | 23 | Python | Statistiche ISTAT via SDMX API |
| [ISTAT MCP](https://github.com/SimonBerg255/istat-mcp) | 3 | Python | 4700+ dataset ISTAT via SDMX, senza API key |
| [ISTAT MCP Server (istatapi)](https://github.com/Halpph/istat-mcp-server) | 2 | Python | Dati statistici ISTAT via libreria Python istatapi |
| [Italy OpenData MCP](https://github.com/stucchi/italy-opendata-mcp) | 1 | Python | Comuni, province, regioni, CAP, coordinate e codici ISTAT/ANPR |
| [OpenData AI](https://github.com/agent-engineering-studio/opendata-ai) | 1 | Python | Multi-source: CKAN, ISTAT, Eurostat, OECD |
| [ISTAT MCP Suite](https://github.com/ManoloZocco/istat-mcp-suite) | 0 | Python | Server unificato per dataset ISTAT |

### ⚖️ Legal-Tech e Normativa

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**BetterCallClaude Italia**](https://github.com/fedec65/bettercallclaude_italia) | 44 | JS | Quadro normativo italiano completo |
| [**MCP Legal IT**](https://github.com/capazme/mcp-legal-it) | 14 | Python | 200+ tool: statuti, giurisprudenza, calcoli legali |
| [Gov IT Legal MCP](https://github.com/SimonBerg255/gov-it-legal-mcp) | 10 | Python | Normattiva + sentenze TAR/CdS |
| [AnonyMCP](https://github.com/avvocati-e-mac/AnonyMCP) | 5 | TS | Pseudonimizza documenti legali prima dell'LLM |
| [Italian Law MCP](https://github.com/Ansvar-Systems/italian-law-mcp) | 1 | TS | GDPR, Codice Privacy, cybercrime |
| [Normattiva MCP](https://github.com/adellorto/normattiva-mcp) | 1 | Python | API di Normattiva |
| [Normattiva MCP (CLI)](https://github.com/avvocati-e-mac/normattiva-mcp) | 0 | Python | CLI + MCP per citare norme da Normattiva.it |

### 🧾 Fatturazione Elettronica

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**Fatture in Cloud MCP**](https://github.com/aringad/fattureincloud-mcp) | 18 | Python | Fatture in Cloud API con Claude AI |
| [Aruba Fatture MCP](https://github.com/MarckDev/aruba-fatture-mcp) | 3 | TS | Aruba Fatturazione Elettronica + SDI |
| [MCP Fattura Elettronica IT](https://github.com/cmendezs/mcp-fattura-elettronica-it) | 1 | Python | Validatore e parser XSD per tracciati XML FatturaPA/SDI |
| [FattureInCloudMCP](https://github.com/badbat75/FattureInCloudMCP) | 0 | TS | Fatture in Cloud API v2, CRUD completo |

### 🏛️ PA, Parlamento e Finanza Pubblica

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [**DoveVannoINostriSoldi**](https://github.com/Italian-Builders-Org/DoveVannoINostriSoldi) | 258 | TS | Spesa pubblica: SIOPE, debito, PNRR, IRPEF e altro — [endpoint remoto](https://www.dovevannoinostrisoldi.com/api/mcp) |
| [**Dichiarino MCP**](https://github.com/gsaccardi/dichiarino-mcp) | 23 | Python | Assistente per la dichiarazione dei redditi |
| [Dati Semantic MCP](https://github.com/italia/dati-semantic-mcp) | 9 | TS | Catalogo semantico Developers Italia, vocabolari e ontologie PA via SPARQL |
| [ANAC MCP](https://github.com/SimonBerg255/anac-mcp) | 4 | Python | Appalti pubblici ANAC (BDNCP) |
| [Italian Parliament MCP](https://github.com/ondata/italianparliament-mcp) | 2 | TS | Dati del Parlamento italiano |
| [RepublicMCP](https://github.com/giuliogarofalo/RepublicMCP) | 1 | TS | Query SPARQL sugli open data di Camera e Senato |
| [Cruscotto Italia MCP](https://cruscotto-italia-mcp.agid.workers.dev/mcp) | 0 | TS | Dati comunali per codice ISTAT: demografia, SIOPE, PNRR, sanità |

### 🛡️ Cybersecurity e Compliance

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [NIS2-public](https://github.com/fabriziosalmi/nis2-public) | 28 | Python | Postura e remediation NIS2 per D.Lgs. 138/2024 e ACN |
| [Italian Competition MCP](https://github.com/Ansvar-Systems/italian-competition-mcp) | 0 | TS | AGCM — decisioni antitrust |
| [Italian Cybersecurity MCP](https://github.com/Ansvar-Systems/italian-cybersecurity-mcp) | 0 | TS | ACN — linee guida e advisory |

### 🎨 Design e Altro

| Progetto | ⭐ | Lang | Descrizione |
|----------|---:|------|-------------|
| [Filo — Design System Italia](https://github.com/Fupete/design-system-italia-mcp) | 3 | TS | Design system .italia (sperimentale) |
| [INGV MCP FDSNWS Event](https://github.com/INGV/mcp-fdsnws-event) | 1 | Python | Dati sismici e eventi in tempo reale via web service INGV |
| [MCP Meteo Italia](https://github.com/makremriahi99/MCP-Meteo-Italia) | 0 | Python | Meteo in tempo reale con FastMCP + Gradio |
<!-- END:catalog -->

### Catalogo in numeri

<!-- BEGIN:stats -->
| Metrica | Valore |
|---------|--------|
| Server totali | **31** |
| Python | 17 |
| TypeScript | 13 |
| JavaScript | 1 |
| Licenze open source | 28 |
| Senza licenza dichiarata | 3 |
| Categorie | 6 |
<!-- END:stats -->

## Dati e API

Il catalogo è disponibile anche in formato machine-readable e viene rigenerato
a ogni aggiornamento di `main`.

```bash
curl -s https://bsab.github.io/italia-mcp-servers/catalog.json \
  | jq '.servers[] | {name, category, url}'
```

| Risorsa | URL |
|---------|-----|
| Catalogo | <https://bsab.github.io/italia-mcp-servers/catalog.json> |
| Schema del catalogo | <https://bsab.github.io/italia-mcp-servers/schema/catalog.schema.json> |
| Schema di un server | <https://bsab.github.io/italia-mcp-servers/schema/server.schema.json> |
| Ricerca e filtri | <https://bsab.github.io/italia-mcp-servers/> |

Il campo `version` indica la versione della struttura del documento e cambia solo
per modifiche incompatibili. Ogni voce di `servers` contiene i campi del file in
`servers/` più `url`, il link canonico del progetto.

## Qualità e trasparenza

L'inclusione nel catalogo **non costituisce una certificazione o approvazione**
del progetto. Prima dell'uso verifica sempre codice, autorizzazioni richieste,
trattamento dei dati e licenza.

Per essere incluso, un server deve:

- implementare il **Model Context Protocol**;
- essere pertinente a dati, norme o servizi italiani;
- fornire almeno un riferimento pubblico tra repository, sito o endpoint MCP;
- avere documentazione d'uso sufficiente.

Le stelle GitHub sono informative e possono non essere aggiornate in tempo
reale. La struttura dei dati viene validata dalla CI; i collegamenti esterni
sono controllati settimanalmente.

## Contribuire

Il modo più semplice è
[proporre un server tramite issue](https://github.com/bsab/italia-mcp-servers/issues/new?template=nuovo-server.yml).
Per aggiungerlo direttamente:

1. crea un file `kebab-case.json` in `servers/`;
2. compilalo secondo [`schema/server.schema.json`](schema/server.schema.json);
3. esegui validazione e generazione;
4. apri una pull request.

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_servers.py
python3 scripts/build_readme.py
```

Le tabelle, i badge e le statistiche racchiusi nei marker `BEGIN`/`END` sono
generati automaticamente: non modificarli a mano. I campi disponibili, le
categorie e i controlli locali sono documentati in [CONTRIBUTING.md](CONTRIBUTING.md).

## Licenza

Questo catalogo è distribuito sotto licenza [MIT](LICENSE).

I singoli server elencati sono sotto le rispettive licenze indicate.

---

<p align="center">
  <i>Fatto in Italia, per rendere dati e servizi italiani accessibili agli assistenti AI.</i>
</p>