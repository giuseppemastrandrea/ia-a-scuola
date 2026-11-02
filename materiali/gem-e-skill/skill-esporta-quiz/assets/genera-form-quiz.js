// ============================================================
//  MOTORE DI GENERAZIONE QUIZ/QUESTIONARIO SU GOOGLE FORM
//  Codice FISSO: non modificare le funzioni.
//  Cambia SOLO le due variabili CONFIG e DOMANDE qui sotto.
//  Esegui la funzione creaForm() e leggi i log per gli URL.
//  Modello per la skill esporta-quiz: __CONFIG__ e __DOMANDE__
//  vengono sostituiti dallo script controlla_quiz.py.
// ============================================================


// ------------------------------------------------------------
//  DATI VARIABILI  (le uniche due cose da cambiare)
// ------------------------------------------------------------
const CONFIG = __CONFIG__;

const DOMANDE = __DOMANDE__;


// ============================================================
//  MOTORE  (codice fisso: non modificare)
// ============================================================

function creaForm() {
  // --- 1. Creazione del form e proprietà di base ---
  const form = FormApp.create(CONFIG.titolo || "Nuovo Form");
  if (CONFIG.descrizione) form.setDescription(CONFIG.descrizione);

  // --- 2. Comportamenti fissi: quiz + identità studente ---
  form.setIsQuiz(true);

  // Raccolta email verificata ristretta al dominio scolastico.
  // NB: setCollectEmail è il metodo corrente; setRequireLogin funziona
  // ma è deprecato (Google potrebbe rimuoverlo). Li isoliamo così un
  // eventuale fallimento non impedisce la creazione del form.
  try {
    form.setCollectEmail(true);
  } catch (e) {
    Logger.log("Avviso: impossibile attivare la raccolta email: " + e);
  }
  try {
    form.setRequireLogin(true);
  } catch (e) {
    Logger.log("Avviso: impossibile restringere al dominio (setRequireLogin): " + e);
  }

  Logger.log("Form creato. Elaborazione delle " + DOMANDE.length + " voci...");

  // --- 3. Costruzione voci, ognuna protetta da try/catch ---
  DOMANDE.forEach(function (dato, index) {
    try {
      costruisciVoce(form, dato, index);
    } catch (error) {
      Logger.log("Voce all'indice " + index + " (" +
                 (dato && dato.tipo) + ") saltata per errore: " + error);
    }
  });

  // --- 4. Output degli URL ---
  Logger.log("==========================================================");
  Logger.log("FORM GENERATO");
  Logger.log("Modifica (docente):      " + form.getEditUrl());
  Logger.log("Compilazione (studenti): " + form.getPublishedUrl());
  Logger.log("==========================================================");
  Logger.log("PROMEMORIA MANUALE: nelle impostazioni del form verifica che");
  Logger.log("1) la raccolta email sia su 'Verificati';");
  Logger.log("2) (se quiz valutato) il rilascio del punteggio sia 'Subito dopo l'invio'.");
  Logger.log("Queste impostazioni l'API di Forms non le espone.");
}


// ------------------------------------------------------------
//  Dispatcher: costruisce una singola voce in base al tipo
// ------------------------------------------------------------

function costruisciVoce(form, dato, index) {
  if (!dato || typeof dato !== "object" || !dato.tipo) {
    Logger.log("Voce all'indice " + index + " ignorata: formato o tipo mancante.");
    return;
  }

  const tipo = dato.tipo;
  const titolo = dato.titolo || "Voce senza titolo";
  const descrizione = dato.descrizione || "";
  const obbligatoria = (dato.obbligatoria !== undefined) ? dato.obbligatoria : true;
  const punti = (typeof dato.punti === "number") ? dato.punti : 0;

  let item;

  switch (tipo) {

    case "text":
      item = form.addTextItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      assegnaPunti(item, punti);
      applicaFeedbackGenerale(item, dato.feedback);
      break;

    case "paragraph":
      item = form.addParagraphTextItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      assegnaPunti(item, punti);
      applicaFeedbackGenerale(item, dato.feedback);
      break;

    case "multipleChoice":
      item = form.addMultipleChoiceItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      assegnaPunti(item, punti);
      impostaScelteSingole(item, dato.opzioni, dato.rispostaCorretta);
      applicaFeedbackScelte(item, dato.feedback);
      break;

    case "list":
      item = form.addListItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      assegnaPunti(item, punti);
      impostaScelteSingole(item, dato.opzioni, dato.rispostaCorretta);
      applicaFeedbackScelte(item, dato.feedback);
      break;

    case "checkbox":
      item = form.addCheckboxItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      assegnaPunti(item, punti);
      impostaScelteMultiple(item, dato.opzioni, dato.rispostaCorretta);
      applicaFeedbackScelte(item, dato.feedback);
      break;

    case "scale":
      item = form.addScaleItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      impostaScala(item, dato.min, dato.max, dato.etichettaMin, dato.etichettaMax);
      assegnaPunti(item, punti);
      applicaFeedbackGenerale(item, dato.feedback);
      break;

    case "grid":
      item = form.addGridItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      impostaGriglia(item, dato.righe, dato.colonne);
      applicaFeedbackGenerale(item, dato.feedback);
      break;

    case "checkboxGrid":
      item = form.addCheckboxGridItem().setTitle(titolo).setRequired(obbligatoria);
      if (descrizione) item.setHelpText(descrizione);
      impostaGriglia(item, dato.righe, dato.colonne);
      applicaFeedbackGenerale(item, dato.feedback);
      break;

    case "sectionHeader":
      item = form.addSectionHeaderItem().setTitle(titolo);
      if (descrizione) item.setHelpText(descrizione);
      break;

    case "pageBreak":
      item = form.addPageBreakItem().setTitle(titolo);
      if (descrizione) item.setHelpText(descrizione);
      break;

    case "image":
      inserisciImmagine(form, dato);
      break;

    case "video":
      inserisciVideo(form, dato);
      break;

    default:
      Logger.log("Avviso: tipo '" + tipo + "' non riconosciuto all'indice " + index + ". Voce saltata.");
  }
}


// ------------------------------------------------------------
//  Helper: punteggio (solo se > 0; isolato per non rompere l'item)
// ------------------------------------------------------------

function assegnaPunti(item, punti) {
  if (typeof punti !== "number" || punti <= 0) return;  // 0 punti -> non chiamare setPoints
  try {
    item.setPoints(punti);
  } catch (e) {
    Logger.log("Nota: punti non applicabili a '" + item.getTitle() + "': " + e);
  }
}


// ------------------------------------------------------------
//  Helper: scelte e correttezza (per indice)
// ------------------------------------------------------------

function impostaScelteSingole(item, opzioni, indiceCorretto) {
  if (!Array.isArray(opzioni) || opzioni.length === 0) return;

  let valida = (typeof indiceCorretto === "number");
  if (valida && (indiceCorretto < 0 || indiceCorretto >= opzioni.length)) {
    Logger.log("Avviso: indice corretto " + indiceCorretto + " fuori range in '" +
               item.getTitle() + "'. Corretta non impostata.");
    valida = false;
  }

  const scelte = opzioni.map(function (op, i) {
    return item.createChoice(op, valida && i === indiceCorretto);
  });
  item.setChoices(scelte);
}

function impostaScelteMultiple(item, opzioni, indiciCorretti) {
  if (!Array.isArray(opzioni) || opzioni.length === 0) return;

  const target = Array.isArray(indiciCorretti) ? indiciCorretti
               : (typeof indiciCorretti === "number" ? [indiciCorretti] : []);

  let valida = target.length > 0;
  for (let k = 0; k < target.length; k++) {
    if (typeof target[k] !== "number" || target[k] < 0 || target[k] >= opzioni.length) {
      Logger.log("Avviso: indice corretto fuori range in '" + item.getTitle() +
                 "'. Corrette non impostate.");
      valida = false;
      break;
    }
  }

  const scelte = opzioni.map(function (op, i) {
    return item.createChoice(op, valida && target.indexOf(i) !== -1);
  });
  item.setChoices(scelte);
}

function impostaScala(item, min, max, etichettaMin, etichettaMax) {
  const lo = (typeof min === "number") ? min : 1;
  const hi = (typeof max === "number") ? max : 5;
  item.setBounds(lo, hi);
  if (etichettaMin || etichettaMax) {
    item.setLabels(etichettaMin || "", etichettaMax || "");
  }
}

function impostaGriglia(item, righe, colonne) {
  if (Array.isArray(righe) && righe.length > 0) item.setRows(righe);
  if (Array.isArray(colonne) && colonne.length > 0) item.setColumns(colonne);
}


// ------------------------------------------------------------
//  Helper: feedback
// ------------------------------------------------------------

function creaFeedback(fb) {
  if (!fb || !fb.testo) return null;
  const builder = FormApp.createFeedback().setText(fb.testo);
  if (fb.link) builder.addLink(fb.link, fb.etichetta || "Approfondisci");
  return builder.build();
}

// Solo per multipleChoice, checkbox, list (auto-corretti)
function applicaFeedbackScelte(item, feedback) {
  if (!feedback) return;
  const c = creaFeedback(feedback.corretto);
  const e = creaFeedback(feedback.errato);
  if (c) item.setFeedbackForCorrect(c);
  if (e) item.setFeedbackForIncorrect(e);
}

// Per gli altri item: feedback generale, con fallback su corretto/errato
function applicaFeedbackGenerale(item, feedback) {
  if (!feedback) return;
  const scelto = feedback.generale || feedback.corretto || feedback.errato;
  const fbObj = creaFeedback(scelto);
  if (!fbObj) return;
  try {
    item.setGeneralFeedback(fbObj);
  } catch (e) {
    Logger.log("Nota: feedback generale non supportato per '" + item.getType() +
               "'. Ignorato.");
  }
}


// ------------------------------------------------------------
//  Helper: media (immagine / video)
// ------------------------------------------------------------

function inserisciImmagine(form, dato) {
  if (!dato.url) {
    Logger.log("Avviso: immagine senza url. Saltata.");
    return;
  }
  // Molti host (es. Wikimedia) bloccano richieste senza User-Agent.
  const resp = UrlFetchApp.fetch(dato.url, {
    headers: { "User-Agent": "Mozilla/5.0 (compatible; GoogleAppsScript)" },
    muteHttpExceptions: true
  });
  if (resp.getResponseCode() !== 200) {
    Logger.log("Avviso: immagine non scaricata (HTTP " + resp.getResponseCode() +
               "): " + dato.url);
    return;
  }
  const img = form.addImageItem().setImage(resp.getBlob());
  if (dato.titolo) img.setTitle(dato.titolo);
  if (dato.descrizione) img.setHelpText(dato.descrizione);
}

function inserisciVideo(form, dato) {
  if (!dato.url) {
    Logger.log("Avviso: video senza url. Saltato.");
    return;
  }
  const vid = form.addVideoItem().setVideoUrl(dato.url);
  if (dato.titolo) vid.setTitle(dato.titolo);
  if (dato.descrizione) vid.setHelpText(dato.descrizione);
}