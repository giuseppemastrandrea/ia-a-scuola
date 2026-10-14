# IA a scuola: catalogo dei moduli

Sito statico per la formazione dei docenti sull'IA generativa: 16 moduli con materiali, esercitazioni pratiche, prompt pronti e un prodotto per ogni modulo. Non ci sono corsi fissi: i percorsi si compongono di volta in volta scegliendo i moduli.

Pubblicato su GitHub Pages: https://giuseppemastrandrea.github.io/ia-a-scuola/. In locale si apre `index.html` nel browser, senza build.

## Struttura

Ogni modulo ha una cartella in `materiali/`, con il nome del modulo e senza numero, così l'indirizzo resta lo stesso anche se l'ordine del catalogo cambia.

| Modulo | Cartella | Contenuto |
|---|---|---|
| M01 Vero, verosimile, falso | `vero-verosimile-falso/` | Deck "Warmup" (falso Eco), quiz "Reale o AI?" in `quiz/` |
| M02 Come funziona un LLM | `come-funziona-llm/` | Deck "Introduzione all'IA e all'IA generativa", simulazione `next-token.html` |
| M03 Testi in serie e bias | `laboratorio-testi-bias/` | Pagina del laboratorio "Mettere le mani" |
| M04 Come si racconta l'IA | (nessuna) | Corpus di 24 articoli nella pagina del catalogo; testi in `../03-risorse/rassegna-m14/`, fuori dal sito |
| M05 Regole e dati | `regole-e-dati/` | Mappa per il docente, vademecum |
| M06 Prompt e contesto | `prompt-e-contesto/` | Deck sul context engineering, esercitazioni "Costruire i profili" e "La storia con GN e GL" |
| M07 Formati di file | `formati-file/` | Solo README: la scheda è nel catalogo |
| M08 NotebookLM | `notebooklm/` | Esercitazione "Il notebook di classe" |
| M09 Gem e skill | `gem-e-skill/` | Esercitazioni "Il mio Gem di sostegno" e "Dal Gem alla skill" |
| M10 Verifiche fino al Google Form | `verifiche-form/` | `genera-form-quiz.gs`: genera un Google Form quiz da `CONFIG` e `DOMANDE` |
| M11 Canvas | `canvas/` | Deck "Gemini Canvas", "Le API", "GitHub Pages"; esercitazioni CAA (completa e semplice), mappa di pittogrammi, mappa con le emoji (infanzia), il mio sito; due risultati d'esempio |
| M12 Canva | `canva/` | In preparazione |
| M13 Scegliere gli strumenti | `scegliere-strumenti/` | Slide "Quattro strati, undici domande" |
| M14 Progettare un'UdA | `progettare-uda/` | In preparazione, prossimo modulo |
| M15 Workspace Studio | `workspace-studio/` | In preparazione |
| M16 Agenti e automazione | `agenti-automazione/` | In preparazione |

`materiali/comune/schemi/` contiene gli schemi SVG usati da più moduli e `genera-schemi.py`, che li rigenera nella stessa cartella.

## Deck

I deck sono sorgenti Marp (`.md`) con HTML e PDF accanto. Per rigenerarli:

```sh
npx @marp-team/marp-cli@4.5.1 --html deck.md -o deck.html < /dev/null
npx @marp-team/marp-cli@4.5.1 --html --pdf --allow-local-files deck.md -o deck.pdf < /dev/null
```

Senza `< /dev/null` Marp può restare in attesa di input.
