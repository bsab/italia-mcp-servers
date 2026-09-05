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
| `python3 -m unittest discover -s scripts -p 'test_*.py'` | Verifica rubrica statica, schemi e rappresentazioni pubbliche senza interrogare server esterni |

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
`site_url`, altrimenti `mcp_endpoint`), e `readiness_score`, calcolato dalla revisione
documentale oppure `null` se non valutato. Il campo `quality_rubric` del catalogo
espone la rubrica condivisa.

## Criteri

- Il server deve implementare il Model Context Protocol
- Deve essere pertinente al contesto italiano
- Deve fornire almeno un riferimento pubblico tra repository, sito o endpoint MCP
- Deve avere documentazione d'uso sufficiente

## Valutazione statica della documentazione

La **prontezza d'uso documentata** è un indice da 0 a 100, non una misura di
popolarità, sicurezza o affidabilità runtime. La revisione legge documentazione
pubblica: non esegue server, non chiama tool MCP e non certifica che le istruzioni
funzionino. Non è un nuovo requisito di ammissione al catalogo.

### Rubrica v1

Ogni criterio riceve `absent` (0), `partial` (metà peso) o `complete` (peso intero).
`absent` significa **non documentato nelle fonti consultate**, non necessariamente
funzionalità assente. Il punteggio è la somma dei contributi, senza arrotondare:
per esempio, compatibilità parziale vale 7,5 punti su 15.

| Criterio | Peso | Completo | Parziale |
|----------|-----:|----------|----------|
| `installation` | 30 | Comandi concreti di installazione e avvio, oppure procedura di connessione remota, senza passaggi operativi da inventare | Accesso o installazione menzionati, ma passaggi operativi incompleti |
| `configuration` | 20 | Runtime, dipendenze e prerequisiti, più variabili e credenziali necessarie (o esplicita assenza di credenziali) | Solo parte dei prerequisiti o della configurazione spiegata |
| `tools` | 20 | Tool o capacità MCP descritti e almeno un esempio concreto di utilizzo, anche un prompt | Solo descrizione delle capacità oppure solo esempio |
| `compatibility` | 15 | Transport MCP esplicito e client identificato con esempio di configurazione o connessione | Solo transport o istruzioni per il client; non dedurre stdio dalla sola sintassi del comando |
| `license` | 10 | Licenza esplicita con testo dei termini accessibile e applicabile al codice del server | Solo nome o badge della licenza, senza termini consultabili |
| `limitations` | 5 | Limite concreto con impatto o alternativa: operazioni non supportate, copertura dati, sola lettura, rate limit | Solo avvertenza generica, per esempio “sperimentale” o “beta” |

Se nessuna delle evidenze indicate è presente, assegnare `absent` motivandolo.
Una semplice ricerca di parole chiave non basta: gli esempi devono riguardare
l'uso MCP, non solo le funzionalità generiche del progetto. Una buona documentazione
può descrivere un server non funzionante; una documentazione scarsa può accompagnare
un buon server. I pesi sono una scelta esplicita del catalogo, non un benchmark validato.

### Registrare una revisione

Il campo opzionale `quality` in `servers/*.json` contiene:

- `rubric_version`: `1`, per rendere esplicito il metodo usato;
- `reviewed_at`: data della consultazione, nel formato `YYYY-MM-DD`;
- `status`: `assessed` oppure `unassessed`;
- per `assessed`, `criteria` con **tutti e sei** i criteri della tabella;
- per ogni criterio: `status`, almeno un URL HTTPS in `evidence` e una motivazione
  originale e specifica in `notes`, anche quando l'esito è `absent`.

Consultare README, documenti pertinenti collegati e testo della licenza. Preferire
URL GitHub fissati al commit, con sezione o righe quando utile, affinché le evidenze
restino verificabili. Non copiare lunghi estratti della documentazione. I metadati
preesistenti del catalogo non sostituiscono le fonti del progetto.

Esempio della struttura di **un singolo criterio**, da ripetere per tutti e sei
con evidenze effettivamente consultate (l'URL qui è dimostrativo):

```json
"compatibility": {
  "status": "partial",
  "evidence": ["https://example.org/documentazione#client"],
  "notes": "È presente una configurazione per un client MCP, ma il transport non è esplicitato."
}
```

Se non è possibile consultare le fonti sufficientemente, **non assegnare zero**.
Omettere `quality` per un server non ancora esaminato; dopo un tentativo di revisione
registrare invece il motivo e le fonti tentate, senza `criteria`:

```json
"quality": {
  "rubric_version": 1,
  "reviewed_at": "2026-09-05",
  "status": "unassessed",
  "reason": "Documentazione pubblica non consultabile durante la revisione; non è possibile assegnare un punteggio.",
  "evidence": ["https://example.org/documentazione"]
}
```

Un errore di recupero delle fonti non dimostra che il progetto sia abbandonato.
La data documenta la revisione, non l'ultimo commit e neppure un health check.
Una nuova revisione deve ricontrollare tutti i criteri e aggiornare data, fonti e
motivazioni; non aggiornare solo la data per far sembrare recente la valutazione.

### Punteggio, ordinamento e trasparenza

Il codice condiviso in [`scripts/quality.py`](scripts/quality.py) calcola il punteggio.
**Non inserire punteggi manuali** nei file dei server. Nel catalogo JSON:

- `quality` conserva la revisione con tutte le evidenze, se disponibile;
- `readiness_score` è un numero tra 0 e 100, oppure `null` per **non valutato**;
- `quality_rubric` espone pesi e significato degli stati per i consumatori dell'API.

Le aggiunte sono compatibili con la versione 1 del catalogo. Le tabelle del README
e il catalogo web ordinano per punteggio decrescente, poi alfabeticamente a parità
di punteggio, con i non valutati in fondo. Un punteggio di zero è una valutazione
completata, distinta dall'assenza di valutazione. Il sito consente anche di filtrare
valutati/non valutati e ordinare per nome. Il punteggio nel README apre il file con
le evidenze; nel sito, i dettagli mostrano ogni criterio e la data della revisione.

Stelle, `featured` e presenza di endpoint remoti **non danno punti** e non decidono
l'ordinamento. `featured` resta una scelta editoriale visibile, l'accesso remoto
un'informazione operativa. Non assegnare badge “healthy” o “stale” sulla base di
questa rubrica o della sola data dell'ultimo commit.

Per correggere una valutazione, aprire una PR con le fonti e la motivazione della
modifica, oppure una segnalazione. Modifiche ai pesi o al significato dei criteri
richiedono una nuova versione della rubrica e la revisione delle valutazioni
esistenti: non ricalcolare silenziosamente giudizi resi con un metodo diverso.

## Segnalare problemi

- Link non funzionanti
- Informazioni errate o obsolete
- Server non più mantenuti

Apri una [issue](https://github.com/bsab/italia-mcp-servers/issues) con i dettagli.