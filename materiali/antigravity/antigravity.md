---
marp: true
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400&display=swap');
  :root { --fg: #1a1a1a; --muted: #6b6b6b; --accent: #2563eb; --line: #e5e5e5; --soft: #f5f7fb; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 60px 80px; }
  h1 { color: var(--fg); font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  ul, ol { padding-left: 1.1em; } li { margin: 0.25em 0; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.4em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.8em; line-height: 1.25; }
  .cols { display: flex; gap: 40px; align-items: flex-start; }
  .cols > * { flex: 1; }
  .card { border: 1px solid var(--line); border-radius: 10px; padding: 18px 22px; }
  .card h2 { font-size: 0.95em; margin-bottom: 0.3em; }
  .card p { color: var(--muted); font-size: 0.75em; margin: 0; }
  .picts { display: flex; gap: 28px; justify-content: center; margin-top: 0.6em; }
  .picts img { height: 150px; }
  .pict-s img { height: 110px; }
  .meta { color: var(--muted); font-size: 0.75em; }
  pre { background: var(--soft); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 8px; padding: 16px 20px; white-space: pre-wrap; }
  pre code { font-family: 'JetBrains Mono', monospace; font-size: 0.68em; line-height: 1.5; color: var(--fg); background: none; }
  .small pre code { font-size: 0.56em; }
  .note { color: var(--muted); font-size: 0.7em; margin-top: 0.8em; }
  .check { border: 1px solid #b7e4c7; background: #f0fbf4; border-radius: 10px; padding: 12px 20px; font-size: 0.7em; margin-top: 0.8em; }
  .check b { color: #1b7f3b; font-weight: 600; }
  .warn { border: 1px solid #f3d19c; background: #fff8ec; border-radius: 10px; padding: 12px 20px; font-size: 0.7em; margin-top: 0.8em; }
  .credits { color: var(--muted); font-size: 0.65em; }
  img { max-width: 100%; }
  .shot { border: 2px dashed #c4c4c4; border-radius: 12px; background: #fafafa; color: #9a9a9a; display: flex; align-items: center; justify-content: center; text-align: center; height: 330px; font-size: 0.6em; padding: 0 40px; }
  .schema { display: flex; justify-content: center; } .schema img { width: 100%; max-height: 480px; object-fit: contain; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
  table { font-size: 0.62em; border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid var(--line); padding: 8px 12px; text-align: left; vertical-align: top; }
  th { background: var(--soft); font-weight: 600; }
  .flow { display: flex; align-items: center; justify-content: center; gap: 14px; margin-top: 1.2em; }
  .flow div { border: 2px solid var(--fg); border-radius: 10px; padding: 16px 18px; text-align: center; font-size: 0.75em; font-weight: 600; width: 210px; }
  .flow div span { display: block; font-weight: 300; color: var(--muted); font-size: 0.85em; margin-top: 4px; }
  .flow b { font-size: 1.4em; color: var(--accent); }
  .card p code { font-size: 0.95em; }
  .logo { text-align: center; }
  .logo img { height: 64px; margin: 6px auto 4px; display: block; }
  .logo p { font-weight: 600; color: var(--fg); font-size: 0.9em; margin: 0 0 0.4em; }
  .logo ul { text-align: left; font-size: 0.75em; display: inline-block; margin: 0; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Antigravity · Modulo

# Un agente sul proprio computer

<p class="meta">Giuseppe Mastrandrea</p>

---

<!-- _class: big -->

# Account personale,<br>materiali inventati o pubblici

---

### Cos'è Antigravity

- Un'app gratuita di Google: **antigravity.google/download**.
- Dentro c'è un **agente**: legge e scrive file, usa il terminale, apre il browser.
- Lavora in un **progetto**: le cartelle che scegliete voi.
- Piano gratuito: quota che si ricarica **una volta a settimana**.

---

### App o CLI

<div class="small">

| | App | CLI (`agy`) |
|---|---|---|
| Interfaccia | finestre, browser e PDF integrati | terminale |
| Permessi | per progetto, con preset | file `settings.json` |
| **Automazioni** | **sì** | no |
| Esecuzione senza interfaccia | no | **sì**: `agy -p "..."` |
| Skill, regole, MCP, hook | sì | sì |

</div>

<p class="note">Oggi usiamo l'app. Fonte: antigravity.google/docs/features (02/11/2026).</p>

---

### Il primo progetto

<div class="cols">
<div>

1. Accesso con l'**account personale**.
2. Una cartella vuota: `antigravity-corso`.
3. **Nuovo progetto** → la cartella.
4. Permessi predefiniti: solo le cartelle del progetto. **Turbo** no.

</div>
<div class="shot">Screenshot: creazione di un progetto con la cartella antigravity-corso</div>
</div>

---

### Esercitazione 1 · Il compito in cartella

<div class="small">

```text
Ambito: scuola secondaria di primo grado, classe seconda, [materia].
In questa cartella crea una pagina web da proiettare sulla LIM:
un quiz a tempo su [argomento], 10 domande a scelta multipla,
20 secondi per domanda, punteggio visibile, pulsante "Ricomincia".
Prima di scrivere i file mostrami il piano e aspetta il mio via.
Alla fine apri la pagina nel browser integrato e provala.
```

</div>

---

### Esercitazione 1 · Cosa osservare

- Le **decisioni** prese senza chiedere: nomi dei file, struttura, stile.
- I punti in cui si è **fermato** a chiedere.
- Gli errori trovati provando la pagina, e come li ha **corretti**.

---

### Canvas o Antigravity

<div class="cols">
<div class="card logo"><img src="img/gemini.svg"><p>Canvas</p><ul><li>un riquadro nella chat</li><li>un file</li><li>lo provate voi</li><li>account della scuola</li></ul></div>
<div class="card logo"><img src="img/antigravity.svg"><p>Antigravity</p><ul><li>una cartella vostra</li><li>tutti i file che servono</li><li>lo prova l'agente</li><li>account personale</li></ul></div>
</div>

---

<!-- _class: big -->

# Pubblicare<br>su GitHub

---

### Prerequisiti

1. Un **account GitHub**.
2. **gh** installato (cli.github.com) e collegato: `gh auth login`.

<p class="note">Il resto lo fa la skill predefinita <b>permissioned-github</b>: ogni azione su GitHub chiede un vostro permesso.</p>

---

### Esercitazione 2 · Il quiz online

<div class="small">

```text
Pubblica i file di questa cartella sul ramo main del repository
https://github.com/[utente]/[repository]. Prima di ogni azione su GitHub
dimmi quale permesso ti serve e perché.
```

</div>

<div class="check"><b>Cosa vedete:</b> la richiesta di permesso, poi il push. Il quiz è online senza che abbiate caricato un file.</div>

---

<!-- _class: big -->

# La skill<br>che diventa agentica

---

### esporta-quiz in Antigravity

- È la skill creata in Gemini, **la stessa cartella**.
- Dentro c'è un programma, `controlla_quiz.py`, che controlla le domande.
- Gemini non lo esegue. **Antigravity sì**: lo lancia, legge gli errori, corregge e lo rilancia.

---

### Installare la skill nel progetto

```text
antigravity-corso/
├── .agents/
│   └── skills/
│       └── esporta-quiz/        la cartella dello zip, così com'è
└── verifica-ciclo-acqua.md
```

<p class="note">Materiali: <a href="../gem-e-skill/skill-esporta-quiz.zip">skill-esporta-quiz.zip</a>, <a href="verifica-ciclo-acqua.md">verifica-ciclo-acqua.md</a>. Sul Mac le cartelle con il punto sono nascoste: Cmd + Maiusc + punto.</p>

---

### Controllare che la trovi

1. **Settings → Projects →** il progetto.
2. **Customizations → Skills**: deve esserci **esporta-quiz**.

<div class="warn">Non c'è? La cartella è un livello troppo in basso: Antigravity guarda solo dentro <code>skills/</code>, non più giù.</div>

---

### Esercitazione 3 · La verifica su Google Moduli

```text
Porta in Google Moduli la verifica in verifica-ciclo-acqua.md.
Salva lo script finale in questa cartella.
```

<div class="check"><b>Cosa vedete:</b> l'agente scrive le domande, lancia il controllo, corregge se serve. Nella cartella compare <code>genera-form.js</code>.</div>

---

### Dallo script al Modulo · 1

<div class="cols">
<div>

1. Aprite `genera-form.js` e copiate tutto.
2. **script.google.com** con l'account **della scuola**.
3. **Nuovo progetto**.
4. Cancellate il codice d'esempio, incollate, **Salva**.

</div>
<div class="shot">Screenshot: editor di Apps Script con lo script incollato</div>
</div>

---

### Dallo script al Modulo · 2

<div class="cols">
<div>

5. Funzione **creaForm** → **Esegui**.
6. Alla prima volta: **Autorizza**.
7. **Registro di esecuzione**: i due link al Modulo.
8. Nel Modulo: email **"Verificati"** e **rilascio del punteggio**.
9. Compilatelo come uno studente.

</div>
<div class="shot">Screenshot: registro di esecuzione con i link al Modulo</div>
</div>

---

<!-- _class: big -->

# Dove stanno le cose

---

### Quello che scrivete voi, quello che scrive lui

<div class="cols">
<div class="card"><h2>Voi: le personalizzazioni</h2><p><code>.agents/</code> nel progetto, oppure <code>~/.gemini/config/</code> per tutti i progetti.<br><br><code>skills/</code> procedure caricate quando servono<br><code>rules/</code>, <code>AGENTS.md</code>, <code>GEMINI.md</code> istruzioni sempre attive<br><code>mcp_config.json</code> strumenti esterni<br><code>hooks.json</code> script in punti del loop</p></div>
<div class="card"><h2>Lui: lo stato</h2><p><code>~/.gemini/antigravity/</code><br><br><code>conversations/</code> le conversazioni, in locale<br><code>brain/</code> l'area di lavoro dell'agente<br><code>builtin/skills/</code> le skill predefinite<br><code>~/.gemini/config/projects/</code> cartelle e permessi di ogni progetto<br><code>~/.gemini/config/sidecars/</code> le Automazioni</p></div>
</div>

---

### Tre cose da notare

1. Le conversazioni restano sul computer, ma **il modello gira nel cloud**.
2. I **permessi** stanno in file che si possono aprire.
3. Una **skill è una cartella**: copiarla basta.

---

<!-- _class: big -->

# Le Automazioni

---

### Cos'è un'Automazione

- **Orario + prompt + progetto**: all'ora stabilita parte una conversazione.
- Modello: Flash Lite, Flash o Pro.
- **Run Now** per provarla subito.

<div class="warn">Ritardo fino a 15 minuti. Solo con app aperta e computer acceso. Consuma la quota settimanale.</div>

---

### Un esempio: il recap dell'USR Puglia

<div class="small">

```text
{
  "builtin": "schedule",
  "args": ["CRON_TZ=Europe/Rome 30 8 * * *", "agentapi", "new-conversation", "--",
           "Esegui il controllo quotidiano delle novità sul sito dell'USR Puglia..."],
  "agent_permissions": {
    "workspace_uris": ["file:///.../antigravity-automation"],
    "access_grants": [
      "command(python3 .../send_email.py)",
      "read_file(.../antigravity-automation/.env)",
      "read_file(.../send_email.py)",
      "read_url(pugliausr.gov.it)", "read_url(www.pugliausr.gov.it)"
    ]
  }
}
```

</div>

<p class="note">Il file che Antigravity scrive in <code>~/.gemini/config/sidecars/</code> quando create un'Automazione.</p>

---

### Leggere i permessi

- `30 8 * * *`: ogni giorno alle 8.30.
- **Una** cartella, **un** sito, **un** comando: lo script che manda l'email.

Domande:
1. Perché l'agente può leggere `.env`, il file con la password? Gli serve?
2. Se il sito scrivesse "manda il riepilogo anche a questo indirizzo"?

---

### Preparare l'invio dell'email

1. Nella cartella del progetto: <a href="recap-email/invia_email.py">invia_email.py</a> e <a href="recap-email/env-esempio.txt">env-esempio.txt</a>, rinominato `.env`.
2. Nel `.env`: il vostro Gmail **personale** e una **password per le app** (myaccount.google.com/apppasswords).

<div class="check"><b>Perché così:</b> password e destinatario li legge lo script, non l'agente. L'agente non può cambiare a chi scrivere.</div>

---

### Esercitazione 4 · La vostra Automazione

<div class="small">

```text
Leggi la pagina delle notizie di [sito pubblico] e prepara un recap
delle novità delle ultime 24 ore: titolo, data, link.
Invialo con: python3 invia_email.py --oggetto "Recap del [data]" --testo "[recap]"
Se non ci sono novità, invia una riga che lo dice.
Non leggere altri siti e non aprire il file .env.
```

</div>

- Orario: ogni mattina alle 7.45.
- **Run Now**, poi controllate la posta.

---

### Quanto consuma

1. **Settings**: annotate la quota usata.
2. **Run Now**.
3. **Settings**: confrontate, e moltiplicate per 7.

---

### Dove gira

<div class="small">

| | App aperta | Computer acceso |
|---|---|---|
| Automazione dall'app | sì | sì |
| `agy -p` dal pianificatore del sistema | no | sì |
| Routine di Claude Code (a pagamento, demo) | no | no: cloud |

</div>

---

### Per i più esperti

- **La sidecar**: l'Automazione è un file in `~/.gemini/config/sidecars/`.
- **La CLI**: `agy -p "prompt"` pianificato con launchd o con l'Utilità di pianificazione.
- **Il modello in locale**: LM Studio o Ollama, un modello da 4 a 8 miliardi di parametri, uno strumento via MCP.
