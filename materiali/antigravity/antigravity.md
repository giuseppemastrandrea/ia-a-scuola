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
  .cols > .sc { flex: 1.2; }
  .sc img { max-height: 420px; max-width: 100%; border: 1px solid var(--line); border-radius: 10px; display: block; margin: 0 auto; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Antigravity · Modulo 1

# Un agente sul proprio computer

<p class="meta">Giuseppe Mastrandrea</p>

---

<!-- _class: big -->

# Account personale,<br>materiali inventati o pubblici

---

### Cos'è Antigravity

<div class="cols">
<div>

- App gratuita di Google: **antigravity.google/download**.
- Dentro c'è un **agente**: file, terminale, browser.
- Lavora in un **progetto**: le cartelle che scegliete voi.
- Quota gratuita **settimanale**.

</div>
<div class="sc"><img src="img/download.png"></div>
</div>

---

### App o CLI

<div class="cols">
<div class="small">

| | App | CLI (`agy`) |
|---|---|---|
| Interfaccia | finestre, browser e PDF integrati | terminale |
| Permessi | per progetto, con preset | file `settings.json` |
| **Automazioni** | **sì** | no |
| Esecuzione senza interfaccia | no | **sì**: `agy -p "..."` |
| Skill, regole, MCP, hook | sì | sì |

</div>
<div class="sc"><img src="img/cli.png"></div>
</div>

<p class="note">Oggi usiamo l'app. Fonte: antigravity.google/docs/features (02/11/2026).</p>

---

### Il primo progetto

<div class="cols">
<div>

1. Accesso con l'**account personale**.
2. Una cartella vuota: `antigravity-corso`.
3. **Create New Project**: l'icona della cartella con il +, accanto a Projects.
4. Permessi: solo le cartelle del progetto, **Turbo** solo qui (slide dopo).

</div>
<div class="sc"><img src="img/nuovo-progetto.png"></div>
</div>

<div class="check"><b>Under the hood:</b> il progetto è un file JSON in <code>~/.gemini/config/projects/</code>: nome, cartella, permessi.</div>

---

### I permessi dell'agente

<div class="small">

| Modalità | Cosa succede |
|---|---|
| **Chiede** (`request-review`) | i comandi aspettano il vostro sì |
| **Nel recinto** (`proceed-in-sandbox`) | i comandi partono da soli, ma chiusi in una sandbox |
| **Turbo** (`always-proceed`) | i comandi partono da soli, senza recinto |

</div>

Oggi: **Turbo, solo in questo progetto**. Settings → Projects → `antigravity-corso` → Auto-Execution Policy. L'impostazione generale resta com'è.

<p class="note">Il primo giorno, su Windows, git chiedeva il permesso a ogni comando: abbiamo passato più tempo a cliccare "Accetta" che a guardare. Fonte delle modalità: la guida integrata di Antigravity (11/11/2026).</p>

---

### Perché di solito Turbo no

<div class="cols">
<div class="card"><h2>Oggi va bene perché</h2><p>la cartella è nuova e vuota<br>l'account è personale<br>i materiali sono inventati o pubblici<br>ogni comando resta scritto nella conversazione</p></div>
<div class="card"><h2>Fuori dal corso, no</h2><p><b>cancella o sovrascrive</b> file senza chiedere<br>una pagina o un documento letto può contenere <b>istruzioni nascoste</b>, e nessuno le ferma<br><b>manda fuori</b> dati (un push, una chiamata) senza che lo vediate<br>i comandi scorrono veloci: <b>smettete di leggerli</b></p></div>
</div>

<div class="warn">Fuori dal corso: <b>Chiede</b>, più un elenco di comandi fidati che partono da soli (Settings → Command Allowlist). Il passo successivo, per git, è nella slide per i più esperti.</div>

---

### I comandi con la barra

<div class="small">

| Comando | Cosa fa | Quando ci serve |
|---|---|---|
| `/plan` | studia il compito e scrive un piano da approvare, prima di toccare i file | il piano prima dell'app |
| `/grill-me` | vi fa domande una alla volta, con una risposta consigliata per ciascuna | prima di scrivere una skill |
| `/btw` | una domanda a parte, senza fermare il lavoro in corso | "cosa stai facendo adesso, e perché?" |
| `/browser` | un agente che naviga e controlla le pagine | provare l'app |
| `/generative_ui` | schemi, grafici e spiegazioni interattive nella chat (solo nell'app) | il confronto con Canvas |
| `/learn` | trasforma le correzioni della sessione in regole o skill, da approvare | dopo aver usato una skill |
| `/plugin` | installa e gestisce i plugin | Modulo 2: Google Docs |
| `/schedule` | un'istruzione a un orario, una volta o a ripetizione | Modulo 2: Automazioni |

</div>

<p class="note">Scrivete <code>/</code> nella casella del messaggio: compare l'elenco con le descrizioni. Fonte: antigravity.google/docs/slash-commands (10/11/2026).</p>

---

### Da usare con cautela

- **`/goal`**: lavora finché l'obiettivo non è raggiunto, **senza fermarsi a chiedere**. Solo con un compito chiaro e una cartella di prova.
- **`/boost`** e **`/teamwork`**: più agenti insieme. Solo nei piani a pagamento.

---

### Prerequisiti per GitHub

1. Un **account GitHub** e un repository vuoto, che raccoglierà tutte le vostre app fatte con Canvas.
2. **git**. Windows: **Git for Windows** (git-scm.com), opzioni predefinite. Mac: nel Terminale scrivete `git` e accettate l'installazione degli strumenti.
3. Solo Mac: **Git Credential Manager**, il pacchetto `.pkg` da github.com/git-ecosystem/git-credential-manager/releases.
4. Nel Terminale (su Windows: Git Bash), una volta sola: `git credential-manager github login`. Si apre il browser, accedete a GitHub e autorizzate.

<p class="note">Senza il passo 4 il push dall'agente non parte: il login nel browser non si apre da solo. Commit e push li fa l'agente con la skill predefinita <b>permissioned-github</b>, anche in Turbo vi dice cosa sta per fare. Pages lo attiviamo a mano.</p>

---

### Esercitazione 1 · L'app in Canvas

In Gemini, account della scuola, con **Canvas** attivo:

<div class="small">

```text
Ambito: scuola secondaria di primo grado, classe seconda, [materia].
Crea un'app da proiettare sulla LIM: un quiz a tempo su [argomento],
10 domande a scelta multipla, 20 secondi per domanda, punteggio visibile,
pulsante "Ricomincia". Tutto in un unico file HTML, senza librerie esterne.
```

</div>

<p class="note">Provatela nel Canvas, poi copiate tutto il codice.</p>

---

### Esercitazione 1 · Dal Canvas a GitHub Pages

In Antigravity, nel progetto `antigravity-corso`:

<div class="small">

```text
Qui sotto c'è il codice di un'app fatta con Gemini Canvas.
Salvalo nella cartella app-canvas con un nome che dica cos'è
(per esempio quiz-ciclo-acqua.html), aprilo nel browser integrato e provalo:
se qualcosa non funziona, correggi e dimmi cosa hai cambiato.
Poi crea o aggiorna app-canvas/index.html: l'elenco di tutte le app della
cartella, con titolo, una riga di descrizione e il link.
Infine commit e push di app-canvas sul ramo main di
https://github.com/[utente]/[repository].
Prima di ogni azione su GitHub dimmi cosa stai per fare e perché.

[il codice copiato dal Canvas]
```

</div>

<div class="check"><b>Cosa vedete:</b> l'app nella cartella, la prova nel browser, l'indice, il push. Poi attiviamo Pages a mano: Settings → Pages → ramo main. L'indirizzo del sito apre l'indice.</div>

<p class="note">Ogni nuova app fatta con Canvas: stesso prompt, e l'indice si aggiorna. Il repository è solo <code>app-canvas/</code>: skill e chiavi del progetto restano fuori.</p>

---

### Esercitazione 1 · Cosa osservare

- Gli errori trovati provando l'app, e come li ha **corretti**.
- Cosa ha **cambiato** rispetto al codice del Canvas.
- I **comandi** che ha lanciato da solo, in Turbo: sono tutti nella conversazione.

---

### Esercitazione 1 · Under the hood

<div class="small">

| Cosa è successo | Dove resta scritto |
|---|---|
| Avete incollato il codice del Canvas | `~/.gemini/antigravity/conversations/[id].db`: la conversazione, sul vostro computer |
| L'agente ha salvato e provato l'app, poi ha aggiornato l'indice | `app-canvas/` nel progetto: i vostri file |
| Ogni comando lanciato (`git add`, `git commit`, `git push`) | `brain/[id]/.system_generated/steps/[n]/output.txt`: **il risultato**, che l'agente rilegge prima della mossa dopo. È il loop |
| Su Windows, git chiedeva il permesso a ogni comando | nella trascrizione (`logs/transcript.jsonl`): il `PATH` modificato davanti a ogni `git` |
| Abbiamo attivato Turbo | `~/.gemini/config/projects/[id].json`: l'impostazione del progetto |

</div>

<p class="note">Aprite le cartelle: Finder → Vai → Vai alla cartella → <code>~/.gemini</code>. Su Windows: <code>%USERPROFILE%\.gemini</code> in Esplora file. Quante azioni sono servite per salvare, provare e pubblicare un file?</p>

---

### Canvas o Antigravity

<div class="cols">
<div class="card logo"><img src="img/gemini.svg"><p>Canvas</p><ul><li>un riquadro nella chat</li><li>un file</li><li>lo provate voi</li><li>account della scuola</li></ul></div>
<div class="card logo"><img src="img/antigravity.svg"><p>Antigravity</p><ul><li>una cartella vostra</li><li>tutti i file che servono</li><li>lo prova e lo pubblica l'agente</li><li>account personale</li></ul></div>
</div>

---

<!-- _class: big -->

# Skill e comportamenti<br>ripetibili

---

### Com'è fatta una skill

```text
nome-della-skill/
├── SKILL.md       obbligatorio: nome, descrizione, istruzioni
├── scripts/       programmi che l'agente esegue
├── references/    documentazione da consultare
├── resources/     modelli e file da riusare
└── examples/      esempi
```

<p class="note">Solo <code>SKILL.md</code> è obbligatorio. I nomi delle cartelle sono quelli suggeriti da Antigravity, ma conta che <code>SKILL.md</code> dica dove guardare: nelle nostre skill troverete <code>doc/</code> e <code>modello.html</code>.</p>

---

### Il file SKILL.md

<div class="small">

```text
---
name: grafici-mermaid
description: Crea mappe concettuali, mappe mentali e linee del tempo con
  Mermaid, per la LIM. Da usare quando l'utente chiede uno di questi grafici.
---

# Grafici Mermaid

1. Leggi solo la pagina di doc/ del tipo di grafico richiesto.
2. Scrivi il grafico in una pagina HTML: caratteri grandi, al massimo 12 nodi, un titolo.
3. Apri la pagina nel browser integrato. Se vedi un errore, correggi e riprova.
```

</div>

<p class="note">In alto, tra i trattini, la <b>descrizione</b>: è la parte più importante, perché è lì che l'agente decide se usare la skill.</p>

---

### Quando entra nel contesto

<div class="flow">
<div>All'inizio<span>nome e descrizione di tutte le skill: poche righe</span></div>
<b>→</b>
<div>Se la richiesta combacia<span>tutto il file SKILL.md</span></div>
<b>→</b>
<div>Solo se serve<span>i file annessi: la documentazione si legge, gli script si eseguono</span></div>
</div>

<p class="note">Antigravity lo chiama <i>progressive disclosure</i>: venti skill installate costano quasi niente finché non servono. Le regole (<code>AGENTS.md</code>, <code>GEMINI.md</code>) invece sono sempre attive.</p>

---

<!-- _class: big -->

# Demo · Una skill<br>con la sua documentazione

---

### Demo · La skill dei grafici

```text
antigravity-corso/
└── .agents/
    └── skills/
        └── grafici-mermaid/
            └── doc/   flowchart.md, mindmap.md, timeline.md, VERSIONE.txt
```

<p class="note">Materiali: <a href="skill-mermaid/grafici-mermaid-doc.zip">grafici-mermaid-doc.zip</a>, la documentazione ufficiale di Mermaid 12.2.0. Manca il file <code>SKILL.md</code>: lo scrive l'agente sul proiettore, voi potete rifarlo a casa.</p>

---

### Demo · Scrivere la skill

<div class="small">

```text
Nella cartella .agents/skills/grafici-mermaid c'è la documentazione ufficiale
di Mermaid per tre tipi di grafico: mappa concettuale (flowchart),
mappa mentale (mindmap) e linea del tempo (timeline). Scrivi il file SKILL.md:
- si usa quando chiedo una mappa concettuale, una mappa mentale o una linea del tempo;
- prima di scrivere un grafico legge solo la pagina di doc/ di quel tipo;
- il grafico va in una pagina HTML che carica Mermaid nella versione di doc/VERSIONE.txt;
- regole per la LIM: caratteri grandi, al massimo 12 nodi, sempre un titolo;
- apre la pagina nel browser integrato e, se vede un errore, corregge e riprova.
Mostrami il SKILL.md prima di salvarlo.
```

</div>

---

### Demo · Usarla

```text
Una mappa mentale sul ciclo dell'acqua per una classe seconda.
```

```text
Ora una linea del tempo delle tappe dell'Unità d'Italia.
```

<div class="check"><b>Cosa vedete:</b> per la mappa mentale apre solo <code>doc/mindmap.md</code>, per la linea del tempo solo <code>doc/timeline.md</code>. La documentazione si carica quando serve, non tutta insieme.</div>

<p class="note">Il PDF: aprite la pagina in Chrome → Stampa → Salva come PDF.</p>

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

### Per i più esperti · Perché git chiedeva sempre

- Su Windows Antigravity **non trovava git**.
- Allora metteva davanti a ogni comando una modifica del `PATH`: la lista delle cartelle in cui Windows cerca i programmi.
- Ogni comando era diverso dal precedente: **"consenti sempre" non valeva mai**.

<p class="note">Succede di solito quando git si installa con Antigravity già aperto.</p>

---

### Per i più esperti · git senza Turbo

<div class="small">

1. Git for Windows con l'opzione predefinita "Git from the command line and also from 3rd-party software".
2. **Chiudete del tutto Antigravity e riapritelo**: il `PATH` lo legge all'avvio.
3. In PowerShell: `where.exe git` deve rispondere `C:\Program Files\Git\cmd\git.exe`.
4. Se non risponde, una volta sola, poi di nuovo il punto 2:

```text
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Program Files\Git\cmd", "User")
```

5. Settings → Command Allowlist: `git`. In `AGENTS.md`: "Usa git direttamente, non modificare PATH".

</div>

<p class="note">Da verificare nella prossima prova: che l'Allowlist accetti <code>git</code> per tutti i sottocomandi.</p>
