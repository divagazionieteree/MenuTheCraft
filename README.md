# Menu Generator per The Craft

Questo progetto contiene programmi Python per convertire i dati del menu dal file Excel "menu The Craft.xlsx" in file HTML responsive ottimizzati per smartphone.

## File inclusi

- `menu_generator.py` - Genera un menu HTML dal primo foglio del file Excel
- `menu_generator_complete.py` - Genera un menu HTML completo da tutti i fogli del file Excel
- `requirements.txt` - Dipendenze Python necessarie
- `menu The Craft.xlsx` - File Excel con i dati del menu
- `venv/` - Ambiente virtuale Python

## Installazione

1. Assicurati di avere Python 3 installato
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
   
   Oppure usa l'ambiente virtuale già creato:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Utilizzo

### Menu singolo (primo foglio)
```bash
python menu_generator.py
```
Genera il file `menu_the_craft.html` dal primo foglio del file Excel.

### Menu completo (tutti i fogli)
```bash
python menu_generator_complete.py
```
Genera il file `menu_completo_the_craft.html` da tutti i fogli del file Excel.

## Caratteristiche del menu HTML generato

- **Design responsive**: Ottimizzato per smartphone e tablet
- **Navigazione**: Link di navigazione tra le sezioni (versione completa)
- **Design moderno**: Gradiente di sfondo, ombre, animazioni
- **Organizzazione**: Sezioni separate per ogni categoria di bevande
- **Prezzi multipli**: Supporto per diverse misure (es. 0.4L, 0.3L, 0.2L)
- **Informazioni complete**: Nome, prezzo, descrizione, birrificio/produttore

## Struttura del file Excel

Il programma riconosce automaticamente le colonne in base ai nomi:
- **Nome prodotto**: colonne contenenti "birra", "bevanda", "nome", "prodotto"
- **Prezzo**: colonne numeriche o contenenti "prezzo", "€", "euro"
- **Descrizione**: colonne contenenti "descrizione", "stile", "dettagli"
- **Produttore**: colonne contenenti "birrificio", "produttore", "brewery"

## Fogli supportati

Il file Excel contiene i seguenti fogli:
1. Birre Spina
2. Bevande
3. Birre Bottiglia
4. Bag in Box
5. Sidri
6. Gin Tonic
7. Amari
8. Liquori
9. Whisky
10. Analcoliche

## Personalizzazione

Per modificare l'aspetto del menu HTML, puoi editare le sezioni CSS nei file Python:
- Colori: modifica i valori hex nel CSS
- Font: cambia la famiglia di font nel `font-family`
- Layout: modifica le dimensioni e spaziature

## Note tecniche

- Il programma usa pandas per leggere i file Excel
- Supporta sia file .xlsx che .xls
- Gestisce automaticamente valori mancanti (NaN)
- Codifica UTF-8 per supportare caratteri speciali italiani
