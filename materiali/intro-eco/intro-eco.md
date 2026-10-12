---
marp: true
paginate: true
size: 16:9
footer: 'La macchina che avrà letto tutto'
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
  section.chi-sono { display: flex; flex-direction: column; justify-content: center; }
  section.chi-sono .bio { display: grid; grid-template-columns: 360px 1fr; gap: 56px; align-items: center; }
  section.chi-sono img.foto { width: 360px; border-radius: 16px; display: block; }
  section.chi-sono h1 { margin-bottom: 14px; }
  section.chi-sono .ruolo { font-size: 0.85em; margin: 6px 0; }
  section.chi-sono .cuore ul { list-style: none; padding: 0; margin: 6px 0 0; }
  section.chi-sono .cuore li { font-size: 0.85em; margin: 0; }
  section.chi-sono .connect { display: flex; align-items: center; gap: 24px; margin-top: 26px; }
  section.chi-sono img.qr { width: 190px; height: 190px; display: block; background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 8px; box-sizing: border-box; }
  section.chi-sono .connect b { display: block; color: var(--fg); font-weight: 600; font-size: 0.8em; }
  section.chi-sono .connect .url { font-family: ui-monospace, monospace; font-size: 0.55em; color: var(--accent); }
  section.chi-sono h3 { font-size: 0.5em; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.6em; }
  section.chi-sono h1 { font-size: 1.7em; }
  section.chi-sono .cuore li { border: 0; padding: 0; }
  .quizqr { display: flex; align-items: center; gap: 56px; }
  .quizqr img { width: 330px; height: 330px; border: 1px solid var(--line); border-radius: 16px; padding: 10px; background: #fff; }
  .quizqr .big { font-size: 1.1em; font-weight: 600; margin: 0 0 0.4em; }
  .quizqr .url { font-family: ui-monospace, monospace; font-size: 0.62em; margin: 0 0 1em; }
  .quizqr .url a { color: var(--accent); text-decoration: none; }
  .det { display: flex; gap: 44px; align-items: center; }
  .det img { height: 470px; border: 1px solid var(--line); border-radius: 10px; }
  .det ul { font-size: 0.8em; }
  .vidbig { display: block; position: relative; width: 760px; margin: 0 auto; }
  .vidbig img { width: 760px; border-radius: 12px; display: block; }
  .vidbig::after { content: ''; position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); border-left: 64px solid rgba(255,255,255,0.92); border-top: 38px solid transparent; border-bottom: 38px solid transparent; filter: drop-shadow(0 0 12px rgba(0,0,0,0.5)); }
  .iglink { text-align: center; font-size: 1.4em; font-weight: 600; margin-top: 1.5em; }
  .iglink a { color: var(--accent); text-decoration: none; border-bottom: 3px solid var(--accent); }
  .det.naz { align-items: stretch; gap: 48px; }
  .det.naz img { height: 480px; width: auto; flex: 0 0 auto; }
  .det.naz > div { display: flex; flex-direction: column; justify-content: space-between; }
  .det.naz ul { font-size: 0.74em; }
  .det.naz li { margin-bottom: 0.7em; }
  .nazlink { margin: 0; padding-left: 0.9em; border-left: 3px solid var(--accent); font-size: 0.74em; font-weight: 600; }
  .nazlink a { color: var(--accent); }
  .year { font-size: 0.55em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.16em; color: var(--accent); margin-bottom: 0.4em; }
---


<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Warmup

12 ottobre 2026

---

<!-- _class: chi-sono -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<div class="bio">
<img class="foto" src="img/giuseppe.png">
<div>

### Chi sono

# Giuseppe Mastrandrea

<div class="ruolo">Docente di informatica</div>
<div class="ruolo">Animatore digitale</div>

<div class="cuore">

* Marito di Carla ❤️❤️

</div>

<div class="connect">
  <img class="qr" src="img/qr_sito.svg" alt="QR code verso giuseppemastrandrea.github.io">
  <div><b>Happy to connect</b><span class="url">giuseppemastrandrea.github.io</span></div>
</div>

</div>
</div>

---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# La macchina che avrà letto tutto

Una Bustina di Minerva di Umberto Eco, L'Espresso, 11 aprile 2010

---

<div class="page">
<img src="img/bustina-falsa.jpg">

<div>

# Leggiamo

Avete la pagina stampata sul banco.

Leggetela per intero, con la penna in mano. Avete dieci minuti.

</div>
</div>

---

# Parliamone

* <b>La tesi</b> cosa sostiene Eco, in una frase?
* <b>Il passaggio</b> quale riga vi ha colpito di più?
* <b>In classe</b> la leggereste ai vostri studenti? Con quale domanda?

---

<!-- _class: cover -->
<!-- _paginate: false -->

# Nel 2010 Eco aveva già capito tutto?

---

<!-- _class: reveal -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# È un falso

Generato con l'intelligenza artificiale e pubblicato su Facebook il 1° ottobre 2026

---

# Ci sono cascati in tanti

<div class="who">

* <img src="img/ritratto-parisi.jpg"><b>Giorgio Parisi</b><span>Nobel per la fisica 2021</span>
* <img src="img/ritratto-floridi.jpg"><b>Luciano Floridi</b><span>filosofo dell'informazione</span>
* <img src="img/ritratto-lipperini.jpg"><b>Loredana Lipperini</b><span>scrittrice e giornalista</span>
* <img src="img/ritratto-neuman.jpg"><b>Andrés Neuman</b><span>scrittore</span>

</div>

<div class="more">

* e con loro lettori, docenti universitari e giornalisti

</div>

<p class="src" style="font-size:0.42em">Fonte: Finestre sull'Arte, Il falso Umberto Eco creato con l'AI · Foto da Wikimedia Commons: Lorenza Parisi (CC BY-SA 4.0), Bigum12 (CC0), Lotta Valente (pubblico dominio), Rodrigo Fernandez (CC BY-SA 3.0)</p>

---

# Indizio 1 · Sotto la M

<div class="zoom">

![w:820](img/dettaglio-m.png)

</div>

<p class="cap">Una stringa di caratteri senza senso: un errore tipico delle immagini generate</p>

---

# Indizio 2 · La data

<div class="zoom">

![w:1000](img/dettaglio-data.png)

</div>

<p class="cap">Secondo Open, un numero dell'Espresso datato 11 aprile 2010 non esiste</p>

---

# Indizio 3 · Una profezia troppo precisa

- <b>Allucinazioni</b> il trattato inventato di Teofrasto di Melitene, con manoscritto e segnatura
- <b>Scuola</b> i temi pieni di «in conclusione possiamo dunque affermare»
- <b>Studenti</b> che chiedono alla macchina «quattro errori, due banalità e un'opinione personale»
- <b>Macchine</b> che imparano da testi scritti da altre macchine

---

# Indizio 4 · La verifica tecnica

- <b>Watermark</b> Open ha controllato l'immagine con lo strumento di OpenAI e ha avuto esito positivo
- <b>Autore</b> Ciro Ascione ha poi rivendicato la paternità del falso

<p class="src">open.online/2026/10/02/umberto-eco-macchina-letto-tutto-ia-fact-check</p>

---

<!-- _class: quote -->

# Il falso spiega se stesso

> Per fare un buon falso bisognava conoscere molto bene il vero; la nuova macchina potrebbe invece democratizzare il falso.

<p class="src">Dal testo della finta Bustina</p>

---

# Ma i falsi non sono una novità

---

<!-- _class: photo -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<img src="img/renzi-crop.jpg">

---

<!-- _class: photo -->
<!-- _paginate: false -->
<!-- _footer: '' -->
<!-- _transition: fade -->

<img src="img/renzi-full.jpg">

---

<!-- _transition: fade -->

<div class="year">Striscia la notizia, 23 settembre 2019</div>

# Il fuori onda di Renzi

<div class="ep">

* <b>Il video</b> un Renzi finto che deride colleghi e governo
* <b>L'etichetta</b> falso sul sito, «esclusiva» in onda
* <b>La diffusione</b> sui social senza contesto, preso per vero
* <b>Il primato</b> primo deepfake famoso in Italia

<div class="vidwrap">

* <a class="vid" href="https://mediasetinfinity.mediaset.it/news/striscialanotizia/com-e-stato-creato-il-fuorionda-con-il-finto-matteo-renzi_SE000000000025_tn5609" target="_blank"><img src="img/video-renzi.jpg"><span>Striscia la notizia, 23 settembre 2019 · 2 min</span></a>

</div>

</div>

---

<div class="year">Dal 2000 a oggi</div>

# "Lentamente muore" non è di Neruda

<div class="ep">

* <b>L'autrice</b> Martha Medeiros, su Zero Hora, nel 2000
* <b>La diffusione</b> email e social la attribuiscono a Neruda
* <b>In Senato</b> Mastella la recita come poesia di Neruda
* <b>Il meccanismo</b> nessun falsario: l'errore si propaga da solo

<a class="vid" href="https://www.youtube.com/watch?v=Dghd7IgsEZg" target="_blank"><img src="img/video-mastella.jpg"><span>Mastella in Senato, gennaio 2008 · 2 min</span></a>

</div>

---

<div class="year">Livorno, luglio 1984</div>

# Le teste di Modigliani

<div class="ep">

* <b>Il contesto</b> centenario: si draga il Fosso Reale
* <b>La burla</b> tre studenti e un trapano Black & Decker
* <b>L'autorità</b> Durbé e Argan le dichiarano autentiche
* <b>La fine</b> i ragazzi confessano a Panorama

<a class="vid" href="https://www.youtube.com/watch?v=gaV4KmSQ8uI" target="_blank"><img src="img/video-modigliani.jpg"><span>Raccolta di servizi tv · 7 min</span></a>

</div>

---

# Cosa serviva per farli?

<div class="tl">
<div class="tl-head"><span class="y">Anno</span><span>Falso</span><span>Cosa serviva</span></div>
<div class="tl-body">
<div class="tl-left">

- <span class="y">1984</span>Teste di Modigliani
- <span class="y">2000</span>"Lentamente muore"
- <span class="y">2019</span>Fuori onda di Renzi
- <span class="y">2026</span>Bustina di Eco

</div>
<div class="tl-right">

- <span class="blank">?</span>
- <span class="blank">?</span>
- <span class="blank">?</span>
- <span class="blank">?</span>

</div>
</div>
</div>

---

# Cosa serviva per farli

<div class="tl">
<div class="tl-head"><span class="y">Anno</span><span>Falso</span><span>Cosa serviva</span></div>
<div class="tl-body">
<div class="tl-left">

- <span class="y">1984</span>Teste di Modigliani
- <span class="y">2000</span>"Lentamente muore"
- <span class="y">2019</span>Fuori onda di Renzi
- <span class="y">2026</span>Bustina di Eco

</div>
<div class="tl-right">

* saper scolpire, un trapano, conoscere lo stile di Modì
* una catena di condivisioni
* una redazione televisiva, tecnici, software specialistico
* <strong>un prompt e mezz'ora</strong>

</div>
</div>
</div>

---

# Cosa resta uguale

| | Eco, 2026 | Modigliani, 1984 |
|---|---|---|
| Cosa si voleva credere | che Eco avesse previsto l'AI | che le teste esistessero, nel centenario |
| Chi ha dato credibilità | Parisi, docenti, giornalisti | Argan, Durbé |
| Come si è scoperto | verifica della fonte | confessione degli autori |

---

<!-- _class: dense -->

# Da goliardata a sistema

* <b>Un falso, una burla</b> le teste di Modigliani: tre studenti, un trapano, un'estate
* <b>Dicembre 2024</b> la Consob oscura sei siti con video falsi di Meloni e Mattarella
* <b>Dal 2025</b> il Vaticano segnala centinaia di canali con discorsi mai pronunciati da Papa Leone XIV
* <b>Il salto</b> dal singolo falso alla produzione in serie, a costo quasi zero

<p class="src">Il Post, 13 dicembre 2024 · ACI Prensa, 2025</p>

---

<!-- _class: act -->
<!-- _paginate: false -->

<p class="act-n">Parte 2</p>

# Come fa una macchina a scrivere come Eco?

---

<!-- _class: quote -->

# Lo dice il falso stesso

> Si obietterà che una successione plausibile di parole non è pensiero.

<p class="src">Dalla finta Bustina. Il falso descrive con precisione come funziona la macchina che l'ha scritto.</p>

---

# Un limite in più: la media

* <b>Il meccanismo</b> scegliere sempre il più probabile porta verso il testo medio
* <b>L'effetto</b> testi corretti, ordinati, intercambiabili: lo stesso post per ogni occasione
* <b>Dopo la pausa</b> lo verifichiamo con le nostre mani

---

<!-- _class: act -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Pausa

---

<!-- _class: act -->
<!-- _paginate: false -->

<p class="act-n">Parte 4</p>

# Riconoscere e verificare

---

# Reale o AI?

<div class="quizqr">
<img src="img/qr-quiz.svg" alt="QR code del quiz">
<div>
<p class="big">Inquadrate il codice</p>
<p class="url"><a href="https://giuseppemastrandrea.github.io/ia-a-scuola/materiali/quiz-reale-o-ai/" target="_blank">giuseppemastrandrea.github.io/ia-a-scuola/<br>materiali/quiz-reale-o-ai</a></p>
<p class="cap" style="text-align:left">12 video. Le soluzioni arrivano alla fine, con le spiegazioni.</p>
</div>
</div>

---

<!-- _class: dense -->

# Come avete fatto?

* <b>Testo nell'immagine</b> scritte storpiate: la maglia del cestista, la stringa sotto la M di Eco
* <b>Corpi e movimenti</b> un tempo le mani; oggi persone che compaiono e scompaiono
* <b>Luci e colori</b> ombre incoerenti, colori troppo uniformi
* <b>Espressioni</b> nei video: enfasi, gesti esagerati
* <b>Bassa qualità</b> telecamere di sorveglianza, video sgranati da cellulare: nascondono i difetti

---

# Indizi, non prove

* <b>I difetti spariscono</b> il NYT ha ripetuto le richieste finché il falso non era pulito
* <b>Il reale inganna</b> il volo in galleria e il minigolf di Zach King erano reali
* <b>La conclusione</b> l'occhio allenato aiuta, ma non basta

---

# E i detector?

<div class="det">
<img src="img/detector-mary-shelley.png" alt="Un detector giudica generato con l'AI un brano di Frankenstein">
<div>

* <b>Il testo</b> l'inizio del capitolo 5 di <i>Frankenstein</i>, Mary Shelley, 1818
* <b>Il verdetto</b> «100% AI GPT»
* <b>L'offerta</b> un pulsante per «umanizzare» il testo
* <b>Il precedente</b> OpenAI ha ritirato il suo rilevatore il 20 luglio 2023 per la «bassa accuratezza»

</div>
</div>

---

# Un'eccezione: SynthID

* <b>Cos'è</b> un watermark invisibile che Google inserisce nelle immagini e nei video generati con i suoi modelli
* <b>Come si usa</b> si carica il file nell'app Gemini e si chiede se è stato creato con l'AI di Google
* <b>Il limite</b> riconosce solo i contenuti di Google: un esito negativo non vuol dire che l'immagine sia reale

<p class="src">Google, «Verify AI-generated images, videos and audio», guida di supporto di Gemini</p>

---

# Il metodo che funziona: la fonte

* <b>Lettura laterale</b> prima di leggere il contenuto, aprire un'altra scheda e chiedersi chi lo pubblica
* <b>Risalire all'originale</b> il numero dell'Espresso, la sentenza, il canale ufficiale
* <b>Il modello Wikipedia</b> ogni affermazione con una fonte verificabile; dal 2023 il progetto AI Cleanup cerca i testi generati
* <b>DigComp 2.2</b> competenza 1.2: valutare dati, informazioni e contenuti digitali

---

<!-- _class: act -->
<!-- _paginate: false -->

<p class="act-n">Parte 5</p>

# Dal falso al normale

---

# Il reel

<p class="iglink"><a href="https://www.instagram.com/reel/DdrqntnO2dQ/" target="_blank">Trend su Instagram</a></p>

---

# La pubblicità

<a class="vidbig" href="https://www.youtube.com/watch?v=VQzN7otcEQA" target="_blank"><img src="img/video-buscopan.jpg" alt="Spot BuscoIBS"></a>

<p class="cap">«BuscoIBS per il Colon Irritabile», spot di Buscopan Italia · 20 secondi · si apre su YouTube</p>

---

# Il giornale

<div class="det naz">
<img src="img/lanazione-ai.png" alt="L'articolo de La Nazione con l'immagine generata con l'AI">
<div>

* <b>15 aprile 2026</b> La Nazione illustra un articolo sulla protesta dei camionisti con un'immagine generata con l'AI, senza dichiararlo
* <b>L'indizio</b> le scritte sui cartelli, il primo dettaglio notato nei commenti
* <b>La segnalazione</b> @oradecima su Instagram: l'immagine viene da un generatore di Google, riconoscibile con SynthID
* <b>Dopo</b> l'immagine è stata sostituita: ora la didascalia dice «Tir in autostrada (foto generica)»

<p class="nazlink"><a href="https://www.lanazione.it/arezzo/cronaca/carburanti-la-rivolta-dei-camionisti-b8445b75" target="_blank">L'articolo oggi</a></p>

</div>
</div>

---

# Ma non parliamone solo male

<p class="iglink"><a href="https://www.instagram.com/gossipgoblin/" target="_blank">instagram.com/gossipgoblin</a></p>

---

# E se l'AI aiutasse chi ha idee ma fatica a esprimerle?

* <b>La domanda</b> chi oggi resta fuori dal dibattito perché non sa scrivere bene?
* <b>La narrazione dei media</b> catastrofe o miracolo: e nel mezzo?

---

# AI e democrazia

<div class="cards two">
<div>

## Restringe il discorso pubblico

Falsi in serie a costo zero, stereotipi amplificati, testi tutti uguali, e il sospetto che **tutto** possa essere falso

</div>
<div class="on">

## Lo allarga

Chi non sa scrivere bene può farsi capire, chi non parla la lingua può partecipare, chi ha un'idea può darle forma

</div>
</div>

---

# La prossima volta

* <b>Progettiamo</b> un'unità didattica di educazione civica su AI e democrazia
* <b>Partiamo</b> dalle implicazioni etiche di ciò che abbiamo visto oggi
* <b>Intanto</b> se volete, provate in classe l'attività del falso Eco

---

# Se portate il falso Eco in classe

* <b>Copie</b> solo cartacee, ritirate a fine lezione: il falso non deve circolare
* <b>Chi capisce subito</b> scrive i sospetti su un foglietto e diventa osservatore
* <b>La sequenza</b> lettura, dibattito, poi la rivelazione: niente ricerche prima, la scoperta arriverebbe in un attimo

---

<!-- _class: fonti -->

# Fonti

- <b>Falso Eco</b> open.online/2026/10/02/umberto-eco-macchina-letto-tutto-ia-fact-check · finestresullarte.info
- <b>Casi</b> pagellapolitica.it (Renzi) · libreriamo.it (Medeiros) · artribune.com (Modigliani) · ilpost.it, 13/12/2024 (Consob) · aciprensa.com (Leone XIV)
- <b>LLM</b> Ted Chiang, The New Yorker, 9/2/2023 · AGI, 28/3/2025 (Tribunale di Firenze)
- <b>Bias</b> «L'intelligenza artificiale generativa è razzista?», ITT Panetti-Pitagora · CNBC, 22/2/2024 (Gemini)
- <b>Verifica</b> Stuart A. Thompson, The New York Times, 29/6/2025 (quiz video) · support.google.com/gemini/answer/16722517 (SynthID) · Decrypt, luglio 2023 (rilevatore OpenAI) · 404 Media (WikiProject AI Cleanup)
