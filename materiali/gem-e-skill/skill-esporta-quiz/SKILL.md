---
name: esporta-quiz
description: Trasforma una verifica o un elenco di domande in uno script di Google Apps Script che crea un Modulo Google in modalità quiz, con risposte corrette, punteggi e feedback. Da usare quando si chiede di portare una verifica in Google Moduli, di creare un quiz su Moduli o di esportare domande a scelta multipla.
---

# Esporta un quiz in Google Moduli

Ambito: verifiche scolastiche dalla primaria alle superiori. Il docente incolla lo script finale su script.google.com con l'account della scuola e lo esegue: il Modulo si crea nel suo Drive.

## Procedura

Copia questo elenco e spunta i passaggi man mano:

```text
[ ] 1. Leggi la verifica e conta le domande
[ ] 2. Scrivi il file domande.json nel formato di assets/esempio-domande.json
[ ] 3. Controlla domande.json (con il programma, se puoi eseguirlo, altrimenti con la lista)
[ ] 4. Se ci sono ERRORI, correggi domande.json e torna al passo 3
[ ] 5. Restituisci lo script completo e le istruzioni per il docente
```

### 1. Leggere la verifica

- Se la verifica non indica la risposta corretta di una domanda, chiedila al docente: non sceglierla tu.
- Se mancano i punti, assegna 1 punto a ogni domanda a risposta chiusa e 0 a quelle aperte, e dillo nella risposta.
- Se nella verifica compaiono nomi di studenti, email o numeri di telefono, toglili e avvisa il docente.

### 2. Scrivere domande.json

Apri `assets/esempio-domande.json` e segui lo stesso formato:

- `config.titolo`: il titolo del Modulo; `config.descrizione`: una o due frasi per gli studenti.
- Ogni domanda ha `tipo`, `titolo`, `obbligatoria`, `punti`.
- Tipi più usati: `multipleChoice` (una risposta), `checkbox` (più risposte), `list` (menu a tendina), `text` (risposta breve), `paragraph` (risposta lunga), `scale`, `pageBreak` (nuova pagina).
- `rispostaCorretta` è l'**indice** dell'opzione giusta e parte da **0**: la prima opzione è 0, la seconda è 1. Per `checkbox` è una lista di indici, per esempio `[0, 2]`.
- `feedback` ha `corretto` ed `errato`, ognuno con un campo `testo` di una riga.
- Mantieni il testo delle domande e delle opzioni come nella verifica del docente: non riscriverlo.

### 3. Controllare

**Se puoi eseguire programmi** (per esempio in Antigravity), esegui:

```text
python3 scripts/controlla_quiz.py domande.json -o genera-form.js
```

Il programma fa i controlli della lista qui sotto e, se non trova errori, monta lo script completo partendo da `assets/genera-form-quiz.js`.

**Se non puoi eseguire programmi** (per esempio nell'app Gemini), controlla ogni domanda con questa lista e scrivi nella risposta che i controlli sono stati fatti a mano.

Errori, da correggere prima di andare avanti:
- `tipo` è uno di questi: multipleChoice, checkbox, list, text, paragraph, scale, grid, checkboxGrid, sectionHeader, pageBreak, image, video;
- ogni domanda ha un `titolo` non vuoto;
- multipleChoice, list e checkbox hanno almeno 2 opzioni, tutte diverse tra loro;
- `rispostaCorretta` è un indice tra 0 e il numero di opzioni meno 1 (per checkbox, una lista di indici diversi);
- una domanda con `punti` maggiori di 0 ha una `rispostaCorretta`;
- `scale` parte da 0 o 1 e arriva a un valore da 3 a 10;
- nessun indirizzo email o numero di telefono nel testo.

Avvisi, da riportare al docente:
- in più di 6 domande su 10 la risposta giusta è nella stessa posizione;
- la risposta giusta è molto più lunga delle altre opzioni;
- manca il feedback `errato` in una domanda con punti.

Poi copia `assets/genera-form-quiz.js` e sostituisci soltanto le due righe `const CONFIG = __CONFIG__;` e `const DOMANDE = __DOMANDE__;` con i dati di domande.json.

### 4. Correggere

Correggi solo gli ERRORI. Gli AVVISI (risposta giusta sempre nella stessa posizione, risposta giusta molto più lunga delle altre, feedback mancanti) vanno riportati al docente, che decide.

## Formato della risposta

1. Una riga con il numero di domande e il punteggio totale.
2. Gli avvisi, se ci sono, e come sono stati fatti i controlli: con il programma o a mano.
3. Lo script completo in un solo blocco di codice.
4. Queste istruzioni, sempre uguali:
   1. Apri script.google.com con l'account della scuola e scegli Nuovo progetto.
   2. Cancella il codice di esempio e incolla tutto lo script.
   3. Salva, scegli la funzione `creaForm` e premi Esegui. Alla prima volta autorizza l'accesso.
   4. Nel Registro di esecuzione trovi i link al Modulo.
   5. Nelle impostazioni del Modulo controlla due cose che lo script non può impostare: raccolta email "Verificati" e rilascio del punteggio.
   6. Compila il Modulo come uno studente e controlla una per una le risposte corrette.

## Errori comuni

- **Indice spostato di 1.** Contare le opzioni da 1 invece che da 0 fa segnare come giusta la risposta sbagliata, per tutta la classe. Ricontrolla ogni `rispostaCorretta` sul testo dell'opzione.
- **Risposta giusta sempre nella stessa posizione.** Se lo script lo segnala, proponi al docente di mescolare le opzioni, aggiornando l'indice.
- **Virgolette nel testo.** Nel JSON le virgolette doppie dentro un testo vanno scritte `\"`: oppure usa quelle basse « ».
- **Correttezza.** I controlli garantiscono la forma, non che la risposta indicata sia giusta: dillo sempre al docente.
