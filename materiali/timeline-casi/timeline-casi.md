---
marp: true
paginate: true
size: 16:9
title: Tre casi in una timeline
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
  :root { --fg: #1a1a1a; --muted: #777; --accent: #2563eb; --line: #e5e5e5; --soft: #e6eeff; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 56px 80px; }
  h1 { font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  li { margin: 0.3em 0; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.4em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.8em; line-height: 1.25; }
  section.big h3 { margin-bottom: 1.2em; }
  .cols { display: flex; gap: 48px; align-items: center; }
  .cols > * { flex: 1; }
  .cols.top { align-items: flex-start; }
  .small { font-size: 0.7em; } .muted { color: var(--muted); }
  img { max-width: 100%; }
  .shot { border: 1px solid var(--line); border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,.08); }

  .passi { display: flex; gap: 18px; margin-top: 0.6em; }
  .passi > div { flex: 1; background: #fafbff; border-top: 4px solid var(--accent); padding: 18px 20px; }
  .passi b { display: block; font-size: 2em; font-weight: 800; color: var(--accent); line-height: 1; }
  .passi p { margin: 0.5em 0 0; font-size: 0.68em; }

  .consegna ul { list-style: none; padding: 0; margin: 0; }
  .consegna li { font-size: 0.95em; font-weight: 400; padding: 14px 0 14px 22px; border-left: 4px solid var(--accent); margin: 0 0 14px; background: #fafbff; }
  .consegna li span { display: block; font-size: 0.65em; font-weight: 300; color: var(--muted); margin-top: 4px; }

  .prompt { background: #f6f7f9; border-left: 4px solid var(--accent); padding: 16px 22px; font-size: 0.6em; font-family: 'Inter', sans-serif; line-height: 1.45; }
  .prompt b { display: block; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.14em; color: var(--muted); margin-bottom: 6px; }
  .warn { background: #fff4d6; border-radius: 10px; padding: 12px 18px; font-size: 0.68em; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Tre casi in una timeline

<p class="muted">Ricostruire un caso con NotebookLM e TimelineJS</p>

<p class="small muted">Rischi degli LLM · Assessment</p>

---

### Assessment

## Il percorso

<div class="passi">
<div><b>1</b><p>Farsi un'idea con Gemini o con la chat di NotebookLM</p></div>
<div><b>2</b><p>Cercare le fonti e scegliere quelle autorevoli</p></div>
<div><b>3</b><p>Copiare il template di TimelineJS e aggiungerlo alle fonti</p></div>
<div><b>4</b><p>Far generare a Gemini il foglio in Studio e importarlo</p></div>
<div><b>5</b><p>Pubblicare il foglio e generare la timeline</p></div>
</div>

---

### Passo 1 · Farsi un'idea

## Prima di cercare le fonti

<div class="cols top">
<div class="small">

- Con **Gemini** o con la chat di **NotebookLM**: chi era, quale chatbot usava, cosa contesta la famiglia, cosa risponde l'azienda
- Queste risposte servono a **orientarsi**: non sono ancora fonti
- Annotate nomi, date e luoghi da verificare al passo 2

</div>
<div class="prompt"><b>Prompt</b>Ambito: ricostruzione di un caso di cronaca per una discussione fra docenti sui rischi dei chatbot.<br><br>Riassumi il caso di [nome] e della causa contro l'azienda del chatbot: chi era, quale chatbot usava, cosa sostiene la famiglia, cosa risponde l'azienda, a che punto è la causa.<br><br>Indica quali punti andrebbero verificati su fonti primarie.</div>
</div>

---

### Passo 2 · Le fonti

## Cercare e scegliere

<div class="cols top">
<div class="small">

**Cercare.** Nel pannello Fonti di NotebookLM usate la ricerca sul web integrata, in modalità rapida o approfondita.

**Scegliere.** Tenete solo quello che regge:

- atti giudiziari e comunicati ufficiali delle aziende;
- testate nazionali e agenzie, con data e firma.

</div>
<div class="small">

**Scartare.** Aggregatori, blog, video senza fonte, articoli che copiano altri articoli.

Per ogni fonte scartata scrivete una riga con il motivo: fa parte della consegna.

**Ogni fatto della timeline deve avere una fonte e una data.**

</div>
</div>

---

### Passo 3 · Il template

## Copiare il template di TimelineJS

<div class="cols">
<div style="flex:1.6"><img class="shot" src="img/template-copia.png"></div>
<div class="small">

- Su [timeline.knightlab.com](https://timeline.knightlab.com) premete "Get the spreadsheet template", poi **Crea una copia**
- Non cambiate le intestazioni, non togliete colonne, non lasciate righe vuote
- Aggiungete la vostra copia **come fonte** del notebook

</div>
</div>

---

### Passo 4 · Studio

## Far generare il foglio a Gemini

<div class="cols">
<div><img class="shot" src="img/studio-prompt.png">

<div class="prompt" style="margin-top:18px"><b>Prompt</b>Ambito: cronologia di un caso di cronaca da pubblicare con TimelineJS.<br><br>Segui il template "Copia di Official TimelineJS3 Template" e crea un file xlsx con la timeline del caso di [nome], usando solo le fonti selezionate. Una riga per evento, date nelle colonne Year, Month e Day, una riga di tipo title in testa. Nel Text di ogni evento cita la fonte con il link.</div>
</div>
<div style="flex:0 0 420px"><img class="shot" src="img/studio-xlsx.png"></div>
</div>

---

### Passo 4 · Studio

## Dall'xlsx al foglio Google

<div class="cols">
<div style="flex:0 0 360px"><img class="shot" src="img/importa-menu.png"></div>
<div><img class="shot" src="img/importa-carica.png"></div>
</div>

<p class="small">Scaricate l'xlsx dal menu ⋮ in Studio. Aprite la vostra copia del template: <strong>File › Importa › Carica</strong>, e scegliete il file.</p>

---

### Passo 4 · Studio

## Sostituire il foglio di lavoro

<div class="cols">
<div style="flex:1.3"><img class="shot" src="img/importa-sostituisci.png"></div>
<div class="small">

- Destinazione: **Sostituisci foglio di lavoro**, poi Importa dati
- Il file resta la vostra copia del template, cambia solo il contenuto

<div class="warn">

Prima di andare avanti controllate il foglio: le date e i link coincidono con le fonti? Gemini ha aggiunto fatti che nelle fonti non ci sono?

</div>

</div>
</div>

---

### Passo 5 · Pubblicare

## Pubblicare il foglio sul web

<div class="cols">
<div><img class="shot" src="img/pubblica-menu.png"></div>
<div><img class="shot" src="img/pubblica-dialogo.png"></div>
</div>

<p class="small"><strong>File › Condividi › Pubblica sul web</strong>, con "Intero documento" e "Pagina web", poi Pubblica.</p>

---

### Passo 5 · Pubblicare

## Copiare il link

<div class="cols">
<div style="flex:0 0 380px"><img class="shot" src="img/pubblica-link.png" style="height:500px"></div>
<div class="small">

- Dopo la pubblicazione compare il link che finisce con **/pubhtml**
- Copiatelo: serve sul sito di TimelineJS

</div>
</div>

---

### Passo 5 · La timeline

## Generare e condividere la timeline

<div class="cols top">
<div><img class="shot" src="img/timeline-genera.png"></div>
<div><img class="shot" src="img/timeline-condividi.png"></div>
</div>

<p class="small">Incollate il link al passo 3 del sito. Al passo 4 aprite l'anteprima e copiate lo <strong>Share link</strong>: è il primo link della consegna.</p>

---

### Assessment

## Cosa consegnate

<div class="consegna">

* Il link alla timeline pubblicata<span>Quello del passo 4 di TimelineJS, "Share link"</span>
* Il link al notebook condiviso<span>Così si vedono le fonti che avete tenuto</span>
* Le fonti scartate e perché<span>Una riga per fonte</span>

</div>

---

<!-- _class: big -->
<!-- _paginate: false -->

### Parliamone

# Portereste l'artefatto in aula?
