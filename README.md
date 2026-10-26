# IA a scuola: catalogo dei moduli

Sito statico per la formazione dei docenti sull'IA generativa: 12 moduli con materiali, esercitazioni pratiche, prompt pronti e un prodotto per ogni modulo. Non ci sono corsi fissi: i percorsi si compongono di volta in volta scegliendo i moduli.

Pubblicato su GitHub Pages: https://giuseppemastrandrea.github.io/ia-a-scuola/. In locale si apre `index.html` nel browser, senza build.

## Struttura

Ogni modulo ha una cartella in `materiali/`, con il nome del modulo e senza numero, così l'indirizzo resta lo stesso anche se l'ordine del catalogo cambia.

| Modulo | Cartella | Contenuto |
|---|---|---|
| M01 Vero, verosimile, falso | `vero-verosimile-falso/` | Deck "Warmup" (falso Eco), quiz "Reale o AI?" in `quiz/` |
| M02 Come funziona un LLM | `come-funziona-llm/` | Deck "Introduzione all'IA e all'IA generativa", simulazione `next-token.html` |
| M03 Il modello nudo | `modello-nudo/` | In preparazione; bozza dell'animazione `manopole.html`, messa da parte |
| M04 Testi in serie e bias | `laboratorio-testi-bias/` | Pagina del laboratorio "Mettere le mani" |
| M05 Regole, dati e strumenti | `regole-e-dati/`, `scegliere-strumenti/` | Mappa per il docente, vademecum, slide "Quattro strati, undici domande" |
| M06 Prompt e contesto | `prompt-e-contesto/` | Deck sul context engineering, esercitazioni "Costruire i profili" e "La storia con GN e GL" |
| M07 Grounding (Gemini Notebook) | `grounding/` | Esercitazione "Il notebook di classe" |
| M08 Gem e skill | `gem-e-skill/` | Esercitazioni "Il mio Gem di sostegno" e "Dal Gem alla skill" |
| M09 Verifiche fino al Google Form | `verifiche-form/` | `genera-form-quiz.gs`: genera un Google Form quiz da `CONFIG` e `DOMANDE` |
| M10 Canvas | `canvas/` | Deck "Gemini Canvas", "Le API", "GitHub Pages"; esercitazioni CAA (completa e semplice), mappa di pittogrammi, "Ogni cosa al suo posto" e "Una storia da completare" (infanzia, semplice e completa), "Indovina e trova" (infanzia), il mio sito; risultati d'esempio |
| M11 Progettare un'UdA | `progettare-uda/` | In preparazione, prossimo modulo |
| M12 Workspace Studio | `workspace-studio/` | In preparazione |

`materiali/comune/schemi/` contiene gli schemi SVG usati da più moduli e `genera-schemi.py`, che li rigenera nella stessa cartella.

Il corpus di 24 articoli (un tempo modulo a sé) è nella pagina del catalogo, sezione `#corpus`, e serve a M11 e M03; i testi sono in `../03-risorse/rassegna-m14/`, fuori dal sito.

## Deck

I deck sono sorgenti Marp (`.md`) con HTML e PDF accanto. Per rigenerarli:

```sh
npx @marp-team/marp-cli@4.5.1 --html deck.md -o deck.html < /dev/null
npx @marp-team/marp-cli@4.5.1 --html --pdf --allow-local-files deck.md -o deck.pdf < /dev/null
```

Senza `< /dev/null` Marp può restare in attesa di input.
