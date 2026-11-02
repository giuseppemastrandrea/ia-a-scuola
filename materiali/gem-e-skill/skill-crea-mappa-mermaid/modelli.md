# Modelli per crea-mappa-mermaid

Un modello per tipo di diagramma. Si parte dal modello e si cambiano testo e numero di caselle.

## Mappa concettuale

```mermaid
flowchart TD
  A["La fotosintesi"] -->|"avviene nelle"| B["Foglie"]
  A -->|"usa"| C["Luce del sole"]
  A -->|"usa"| D["Acqua e anidride carbonica"]
  A -->|"produce"| E["Zuccheri"]
  A -->|"libera"| F["Ossigeno"]
  B -->|"contengono la"| G["Clorofilla"]
```

## Mappa mentale

```mermaid
mindmap
  root((Autunno))
    Natura
      Foglie
      Castagne
    Tempo
      Pioggia
      Nebbia
    Animali
      Scoiattolo
      Riccio
```

## Linea del tempo

```mermaid
timeline
  title La Rivoluzione francese
  1789 : Presa della Bastiglia : Dichiarazione dei diritti
  1792 : Nasce la Repubblica
  1793 : Inizia il Terrore
  1799 : Colpo di Stato di Napoleone
```

## Diagramma di flusso

```mermaid
flowchart TD
  A(["Inizio"]) --> B["Leggi a, b, c"]
  B --> C{"Delta maggiore di zero?"}
  C -->|"Sì"| D["Due soluzioni"]
  C -->|"No"| E{"Delta uguale a zero?"}
  E -->|"Sì"| F["Una soluzione"]
  E -->|"No"| G["Nessuna soluzione reale"]
  D --> H(["Fine"])
  F --> H
  G --> H
  class A,H inizio
  class C,E domanda
  class B,D,F,G passo
  classDef inizio fill:#d9f2e6,stroke:#1b7f3b,color:#1a1a1a
  classDef domanda fill:#fff4d6,stroke:#b7791f,color:#1a1a1a
  classDef passo fill:#e6eefc,stroke:#2563eb,color:#1a1a1a
```

## Schema causa-effetto

```mermaid
flowchart LR
  A["Disboscamento"] --> D["Meno alberi"]
  B["Incendi"] --> D
  D --> E["Meno anidride carbonica assorbita"]
  E --> F["Aumento della temperatura"]
  C["Traffico e industrie"] --> G["Più anidride carbonica nell'aria"]
  G --> F
  class A,B,C inizio
  class D,E,G passo
  class F domanda
  classDef inizio fill:#d9f2e6,stroke:#1b7f3b,color:#1a1a1a
  classDef domanda fill:#fff4d6,stroke:#b7791f,color:#1a1a1a
  classDef passo fill:#e6eefc,stroke:#2563eb,color:#1a1a1a
```

Nello schema causa-effetto il colore giallo segna l'effetto finale, il verde le cause di partenza.
