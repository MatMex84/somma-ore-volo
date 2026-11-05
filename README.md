# Somma ore di volo

Applicazione web a pagina unica: si carica il **Flight Pilot Log** in PDF e si ottiene la somma delle ore di volo **dopo l'abilitazione**, con il riepilogo per tipo di attività (SOC, IST, SCU, ADD, CON…). La scuola iniziale viene mostrata a parte e non viene sommata.

## Uso
Apri `index.html` in un browser (nessuna installazione, funziona anche offline) e scegli o trascina il PDF. Il file resta sul dispositivo: non viene inviato da nessuna parte.

## Regole di calcolo
- Per ogni volo si legge la colonna **TOTALE**; se è vuota (PDF più vecchi) si usa il tempo singolo.
- **Data di abilitazione**: si inserisce a mano dopo aver caricato il PDF; finché non c'è, non viene mostrato nessun numero. Il conteggio parte dal giorno successivo: i voli fino a quella data compresa sono scuola iniziale e non vengono sommati.
- Ore dopo l'abilitazione = voli con data successiva alla data indicata. La scuola successiva (SCU) resta conteggiata.
- Controllo automatico: ore dopo abilitazione + scuola iniziale = "Total next Month" dell'ultima pagina del PDF.

## Sviluppo
`src/template.html` contiene interfaccia e logica; `build.py` incorpora pdf.js (3.11.174) e genera `index.html`.

```
npm install
python3 build.py
```

Limiti: servono PDF con testo selezionabile (niente OCR); se il formato del log cambia, le righe non lette vengono segnalate.

## Copyright
Copyright (c) 2026 Matteo Messina. Tutti i diritti riservati.
