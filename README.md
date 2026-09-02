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

<!-- BEGIN:catalog -->
### 📊 Dati e Statistiche

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/ondata/ckan-mcp-server"><strong>CKAN MCP Server</strong></a></td>
    <td align="right">57</td>
    <td>TS</td>
    <td>Connettore generico per istanze CKAN (dati.gov.it e portali regionali)</td>
    <td align="center"><a href="https://ckan-mcp-server.andy-pr.workers.dev/mcp"><img src="https://img.shields.io/badge/Connetti-0969da?style=flat-square" alt="Connetti"></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/ondata/istat_mcp_server"><strong>ISTAT MCP Server</strong></a></td>
    <td align="right">23</td>
    <td>Python</td>
    <td>Statistiche ISTAT via SDMX API</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SimonBerg255/istat-mcp">ISTAT MCP</a></td>
    <td align="right">3</td>
    <td>Python</td>
    <td>4700+ dataset ISTAT via SDMX, senza API key</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Halpph/istat-mcp-server">ISTAT MCP Server (istatapi)</a></td>
    <td align="right">2</td>
    <td>Python</td>
    <td>Dati statistici ISTAT via libreria Python istatapi</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/stucchi/italy-opendata-mcp">Italy OpenData MCP</a></td>
    <td align="right">1</td>
    <td>Python</td>
    <td>Comuni, province, regioni, CAP, coordinate e codici ISTAT/ANPR</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/agent-engineering-studio/opendata-ai">OpenData AI</a></td>
    <td align="right">1</td>
    <td>Python</td>
    <td>Multi-source: CKAN, ISTAT, Eurostat, OECD</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/ManoloZocco/istat-mcp-suite">ISTAT MCP Suite</a></td>
    <td align="right">0</td>
    <td>Python</td>
    <td>Server unificato per dataset ISTAT</td>
    <td align="center">—</td>
  </tr>
  </tbody>
</table>

### ⚖️ Legal-Tech e Normativa

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/fedec65/bettercallclaude_italia"><strong>BetterCallClaude Italia</strong></a></td>
    <td align="right">44</td>
    <td>JS</td>
    <td>Quadro normativo italiano completo</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/capazme/mcp-legal-it"><strong>MCP Legal IT</strong></a></td>
    <td align="right">14</td>
    <td>Python</td>
    <td>200+ tool: statuti, giurisprudenza, calcoli legali</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SimonBerg255/gov-it-legal-mcp">Gov IT Legal MCP</a></td>
    <td align="right">10</td>
    <td>Python</td>
    <td>Normattiva + sentenze TAR/CdS</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/avvocati-e-mac/AnonyMCP">AnonyMCP</a></td>
    <td align="right">5</td>
    <td>TS</td>
    <td>Pseudonimizza documenti legali prima dell&#x27;LLM</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Ansvar-Systems/italian-law-mcp">Italian Law MCP</a></td>
    <td align="right">1</td>
    <td>TS</td>
    <td>GDPR, Codice Privacy, cybercrime</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/adellorto/normattiva-mcp">Normattiva MCP</a></td>
    <td align="right">1</td>
    <td>Python</td>
    <td>API di Normattiva</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/avvocati-e-mac/normattiva-mcp">Normattiva MCP (CLI)</a></td>
    <td align="right">0</td>
    <td>Python</td>
    <td>CLI + MCP per citare norme da Normattiva.it</td>
    <td align="center">—</td>
  </tr>
  </tbody>
</table>

### 🧾 Fatturazione Elettronica

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/aringad/fattureincloud-mcp"><strong>Fatture in Cloud MCP</strong></a></td>
    <td align="right">18</td>
    <td>Python</td>
    <td>Fatture in Cloud API con Claude AI</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/MarckDev/aruba-fatture-mcp">Aruba Fatture MCP</a></td>
    <td align="right">3</td>
    <td>TS</td>
    <td>Aruba Fatturazione Elettronica + SDI</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/cmendezs/mcp-fattura-elettronica-it">MCP Fattura Elettronica IT</a></td>
    <td align="right">1</td>
    <td>Python</td>
    <td>Validatore e parser XSD per tracciati XML FatturaPA/SDI</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/badbat75/FattureInCloudMCP">FattureInCloudMCP</a></td>
    <td align="right">0</td>
    <td>TS</td>
    <td>Fatture in Cloud API v2, CRUD completo</td>
    <td align="center">—</td>
  </tr>
  </tbody>
</table>

### 🏛️ PA, Parlamento e Finanza Pubblica

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/Italian-Builders-Org/DoveVannoINostriSoldi"><strong>DoveVannoINostriSoldi</strong></a></td>
    <td align="right">258</td>
    <td>TS</td>
    <td>Spesa pubblica: SIOPE, debito, PNRR, IRPEF e altro</td>
    <td align="center"><a href="https://www.dovevannoinostrisoldi.com/api/mcp"><img src="https://img.shields.io/badge/Connetti-0969da?style=flat-square" alt="Connetti"></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/gsaccardi/dichiarino-mcp"><strong>Dichiarino MCP</strong></a></td>
    <td align="right">23</td>
    <td>Python</td>
    <td>Assistente per la dichiarazione dei redditi</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/italia/dati-semantic-mcp">Dati Semantic MCP</a></td>
    <td align="right">9</td>
    <td>TS</td>
    <td>Catalogo semantico Developers Italia, vocabolari e ontologie PA via SPARQL</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SimonBerg255/anac-mcp">ANAC MCP</a></td>
    <td align="right">4</td>
    <td>Python</td>
    <td>Appalti pubblici ANAC (BDNCP)</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/ondata/italianparliament-mcp">Italian Parliament MCP</a></td>
    <td align="right">2</td>
    <td>TS</td>
    <td>Dati del Parlamento italiano</td>
    <td align="center"><a href="https://italianparliament-mcp.andy-pr.workers.dev/mcp"><img src="https://img.shields.io/badge/Connetti-0969da?style=flat-square" alt="Connetti"></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/giuliogarofalo/RepublicMCP">RepublicMCP</a></td>
    <td align="right">1</td>
    <td>TS</td>
    <td>Query SPARQL sugli open data di Camera e Senato</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://cruscotto-italia-mcp.agid.workers.dev/mcp">Cruscotto Italia MCP</a></td>
    <td align="right">0</td>
    <td>TS</td>
    <td>Dati comunali per codice ISTAT: demografia, SIOPE, PNRR, sanità</td>
    <td align="center"><a href="https://cruscotto-italia-mcp.agid.workers.dev/mcp"><img src="https://img.shields.io/badge/Connetti-0969da?style=flat-square" alt="Connetti"></a></td>
  </tr>
  </tbody>
</table>

### 🛡️ Cybersecurity e Compliance

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/fabriziosalmi/nis2-public">NIS2-public</a></td>
    <td align="right">28</td>
    <td>Python</td>
    <td>Postura e remediation NIS2 per D.Lgs. 138/2024 e ACN</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Ansvar-Systems/italian-competition-mcp">Italian Competition MCP</a></td>
    <td align="right">0</td>
    <td>TS</td>
    <td>AGCM — decisioni antitrust</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Ansvar-Systems/italian-cybersecurity-mcp">Italian Cybersecurity MCP</a></td>
    <td align="right">0</td>
    <td>TS</td>
    <td>ACN — linee guida e advisory</td>
    <td align="center">—</td>
  </tr>
  </tbody>
</table>

### 🎨 Design e Altro

<table width="100%">
  <thead>
    <tr>
      <th width="24%">Progetto</th>
      <th width="8%" align="right">⭐</th>
      <th width="10%">Lang</th>
      <th width="46%">Descrizione</th>
      <th width="12%">Connetti</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://github.com/Fupete/design-system-italia-mcp">Filo — Design System Italia</a></td>
    <td align="right">3</td>
    <td>TS</td>
    <td>Design system .italia (sperimentale)</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/INGV/mcp-fdsnws-event">INGV MCP FDSNWS Event</a></td>
    <td align="right">1</td>
    <td>Python</td>
    <td>Dati sismici e eventi in tempo reale via web service INGV</td>
    <td align="center">—</td>
  </tr>
  <tr>
    <td><a href="https://github.com/makremriahi99/MCP-Meteo-Italia">MCP Meteo Italia</a></td>
    <td align="right">0</td>
    <td>Python</td>
    <td>Meteo in tempo reale con FastMCP + Gradio</td>
    <td align="center">—</td>
  </tr>
  </tbody>
</table>
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