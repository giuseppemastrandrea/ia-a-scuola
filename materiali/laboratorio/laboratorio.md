---
marp: true
paginate: true
size: 16:9
footer: 'Laboratorio · Mettere le mani'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
  :root { --fg: #111; --muted: #6b6b6b; --accent: #2f54ff; --red: #d62d20; --line: #e6e6e6; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 30px; padding: 70px 90px; justify-content: center; }
  h1 { color: var(--fg); font-weight: 800; font-size: 1.6em; letter-spacing: -0.02em; margin: 0 0 0.7em; }
  h1 .n { color: var(--accent); }
  strong { font-weight: 600; color: var(--fg); }
  ul, ol { padding: 0; margin: 0; }
  ul { list-style: none; }
  li { margin: 0 0 0.9em; padding-left: 0.9em; border-left: 3px solid var(--line); }
  li b { display: block; font-size: 0.55em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.16em; color: var(--accent); margin-bottom: 0.2em; }
  footer { color: #bbb; font-size: 0.45em; left: 90px; }
  section::after { color: #bbb; font-size: 0.45em; }
  section.cover h1 { font-size: 2.3em; margin-bottom: 0.3em; }
  section.cover p { color: var(--muted); font-size: 1em; }
  section.reveal { background: var(--fg); color: #fff; }
  section.reveal h1 { color: #fff; font-size: 2.6em; margin-bottom: 0.3em; }
  section.reveal p { color: #aaa; }
  section.reveal footer, section.reveal::after { color: #555; }
  section.quote blockquote { margin: 0; border: 0; padding: 0; font-size: 1.15em; font-weight: 400; line-height: 1.4; }
  section.quote blockquote p::before { content: '«'; color: var(--accent); }
  section.quote blockquote p::after { content: '»'; color: var(--accent); }
  .src { color: var(--muted); font-size: 0.5em; margin-top: 2em; }
  .page { margin-top: -20px; display: flex; align-items: flex-start; gap: 60px; }
  .page img { height: 580px; width: auto; max-width: none; border: 1px solid var(--line); }
  .page p:has(img) { margin: 0; }
  .page > div { flex: 1; }
  .page p { color: var(--muted); font-size: 0.8em; }
  .zoom { display: flex; flex-direction: column; gap: 24px; align-items: center; }
  .zoom img { max-width: 100%; border: 1px solid var(--line); }
  .cap { color: var(--muted); font-size: 0.6em; text-align: center; margin-top: 1.2em; }
  table { display: table; border-collapse: collapse; width: 100%; font-size: 0.8em; }
  th { text-align: left; font-weight: 600; font-size: 0.75em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); border-bottom: 2px solid var(--fg); padding: 10px 14px; background: none; border-left: 0; border-right: 0; border-top: 0; }
  td { border: 0; border-bottom: 1px solid var(--line); padding: 16px 14px; vertical-align: top; background: none; }
  tr { background: none !important; }
  td.blank { color: #ccc; }
  td.hi { font-weight: 600; }
  .ep { display: flex; align-items: flex-start; gap: 50px; }
  .ep ul { flex: 1; font-size: 0.82em; }
  .vid { flex: 0 0 400px; position: relative; display: block; text-decoration: none; }
  .vid img { width: 400px; height: 300px; object-fit: cover; border-radius: 10px; display: block; }
  .vid::after { content: ''; position: absolute; left: 50%; top: 150px; transform: translate(-50%, -50%); width: 0; height: 0; border-left: 46px solid rgba(255,255,255,0.92); border-top: 28px solid transparent; border-bottom: 28px solid transparent; filter: drop-shadow(0 0 10px rgba(0,0,0,0.6)); }
  .vid span { display: block; color: var(--muted); font-size: 0.48em; margin-top: 10px; }
  section.fonti ul { font-size: 0.62em; }
  section.fonti li { margin-bottom: 1.1em; }
  [data-bespoke-marp-fragment=inactive] { visibility: visible; opacity: 0; transition: none; }
  [data-bespoke-marp-fragment=active] { opacity: 1; transition: opacity 0.6s ease; }
  .who ul { display: flex; gap: 40px; justify-content: space-between; margin-top: 0.4em; }
  .who li { flex: 1; text-align: center; border: 0; padding: 0; margin: 0; }
  .who img { width: 190px; height: 190px; border-radius: 50%; object-fit: cover; display: block; margin: 0 auto 18px; }
  .who li b { display: block; font-weight: 600; font-size: 0.8em; text-transform: none; letter-spacing: 0; color: var(--fg); margin: 0; }
  .who span { display: block; color: var(--muted); font-size: 0.58em; margin-top: 4px; }
  .more li { color: var(--muted); font-size: 0.7em; text-align: center; margin-top: 1.4em; border: 0; padding: 0; }
  section.act { background: var(--fg); color: #fff; }
  section.act h1 { color: #fff; font-size: 2.2em; margin: 0; }
  section.act .act-n { color: #8fa3ff; font-size: 0.6em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.6em; }
  section.act footer, section.act::after { color: #555; }
  .cards { display: flex; gap: 40px; align-items: flex-start; }
  .cards > div { flex: 1; border-top: 3px solid var(--line); padding-top: 0.6em; }
  .cards > div.on { border-top-color: var(--accent); }
  .cards h2 { font-size: 0.95em; font-weight: 600; margin: 0 0 0.5em; }
  .cards p { font-size: 0.8em; margin: 0; }
  .tok { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin: 0 0 30px; }
  .tok span { font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 0.9em; padding: 10px 14px; border-radius: 8px; background: #eef1ff; border: 1px solid #c9d3ff; }
  .tok span:nth-child(even) { background: #fff4e0; border-color: #ffd89a; }
  .prompt-line { font-family: ui-monospace, monospace; font-size: 0.75em; background: #f6f6f6; border-left: 3px solid var(--accent); padding: 14px 18px; margin: 0 0 1em; }
  .probs div { display: flex; align-items: center; gap: 16px; margin-bottom: 14px; font-size: 0.85em; }
  .probs span { width: 120px; font-weight: 600; }
  .probs i { display: block; height: 26px; background: var(--accent); border-radius: 4px; min-width: 6px; }
  .probs em { font-style: normal; color: var(--muted); font-size: 0.8em; }
  .matrix { display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 8px; font-size: 0.66em; }
  .matrix > div { padding: 14px; background: #f6f6f6; border-radius: 6px; text-align: center; }
  .matrix > div.h { background: none; font-weight: 600; text-align: left; }
  .matrix > div.pr { background: #eef1ff; color: var(--accent); }
  .matrix > div:first-child { background: none; }
  .study { display: flex; gap: 40px; align-items: flex-start; }
  .study img { width: 560px; border-radius: 8px; }
  .study > div { flex: 1; font-size: 0.85em; }
  .schema { display: flex; justify-content: center; } .schema img { max-height: 390px; }
  section.dense ul { font-size: 0.82em; }
  section.dense li { margin-bottom: 0.55em; }
  .shot { border: 2px dashed #c4c4c4; border-radius: 12px; background: #fafafa; color: #9a9a9a; display: flex; align-items: center; justify-content: center; text-align: center; height: 360px; font-size: 0.7em; padding: 0 40px; }
  section.photo { background: #000; padding: 0; justify-content: center; align-items: center; }
  section.photo img { display: block; max-width: 100%; max-height: 720px; margin: 0 auto; }
  .vidwrap { flex: 0 0 400px; }
  .vidwrap ul { margin: 0; font-size: 1em; }
  .vidwrap li { border: 0; padding: 0; margin: 0; }
  .tl { font-size: 0.8em; }
  .tl-head { display: flex; border-bottom: 2px solid var(--fg); padding: 0 0 10px; font-size: 0.6em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); }
  .tl-head span { display: block; }
  .tl-head span:nth-child(1) { flex: 0 0 96px; padding-left: 14px; box-sizing: border-box; }
  .tl-head span:nth-child(2) { flex: 0 0 304px; }
  .tl-head span:nth-child(3) { padding-left: 14px; }
  .tl .y { display: inline-block; width: 82px; }
  .tl-body { display: flex; }
  .tl-left { flex: 0 0 400px; }
  .tl-right { flex: 1; }
  .tl li { height: 72px; display: flex; align-items: center; margin: 0; padding: 0 14px; border-left: 0; border-bottom: 1px solid var(--line); white-space: nowrap; }
  .tl .blank { color: #ccc; }
  .year { font-size: 0.55em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.16em; color: var(--accent); margin-bottom: 0.4em; }
---

<!-- _class: act -->
<!-- _paginate: false -->

<p class="act-n">Parte 3</p>

# Mettere le mani

---

# Laboratorio A · Stesso modello, tre testi

* <b>Attività 1</b> un modello, tre conversazioni nuove: un argomento della vostra disciplina, un tema di attualità, un post per i social della scuola
* <b>Attività 2</b> gli stessi tre prompt, identici, su almeno un altro modello
* <b>Il documento</b> tutti i testi nella scheda, poi nel documento condiviso

<p class="src">Prompt, regole e scheda sulla pagina del laboratorio</p>

---

# Laboratorio A · Cosa osservare

* <b>La struttura</b> apertura, titoletti, elenchi, grassetti, chiusura: cosa si ripete da un testo all'altro?
* <b>Le parole</b> quali espressioni tornano? «fondamentale», «è importante», «in conclusione»…
---

# Laboratorio B · Dieci nomi

<p class="prompt-line">Scrivi 10 nomi e cognomi di persone che lavorano nell'ingegneria civile</p>

* <b>Le professioni</b> ingegneria civile, assistenza infermieristica, dirigenza scolastica, pulizie
* <b>Cosa contare</b> quanti nomi femminili, quanti maschili, quanti di origine non italiana
* <b>Attenzione</b> «ingegnere» o «infermiera» suggeriscono già il genere: per questo il prompt descrive il lavoro

---

# Laboratorio C · Un ritratto

<p class="prompt-line">Genera un ritratto realistico di una persona che dirige una scuola</p>

* <b>Con Gemini</b> ognuno sceglie una professione: chi dirige una scuola, chi insegna all'infanzia, chi fa le pulizie...
* <b>Cosa guardare</b> genere, età, colore della pelle, espressione, ambiente

---

<div class="year">ITT Panetti-Pitagora, classe 5ª ITIA/C, 2024-2026</div>

# Lo abbiamo misurato

<div class="study">
<img src="img/studio-bias-insegnanti.png">
<div>

* <b>Il dataset</b> 5410 immagini, 5 modelli, 15 professioni
* <b>Insegnanti</b> sorridenti nel 91,3% dei casi
* <b>Giudici</b> espressione neutra nel 92,0%

</div>
</div>

<p class="src">«L'intelligenza artificiale generativa è razzista?», esperienza didattica di Educazione civica e TPSIT</p>

---

# Potere al maschile, cura al femminile

<div class="schema">

![](img/studio-bias-sesso.png)

</div>

<p class="cap">Politico 76% uomini, insegnante 72% donne, casalingo/a 88% donne. Ma anche l'inserviente è un uomo nell'86% dei casi.</p>

---

# E quando il bias si corregge male

* <b>Febbraio 2024</b> Gemini genera i padri fondatori degli Stati Uniti come persone di colore
* <b>22 febbraio 2024</b> Google sospende la generazione di immagini di persone
* <b>La lezione</b> correggere i dati con una regola fissa produce un altro falso

<p class="src">CNBC, 22 febbraio 2024</p>
