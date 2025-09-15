#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menu Generator Complete - Converte tutti i fogli Excel in HTML responsive per smartphone
"""

import pandas as pd
import os
import base64
from datetime import datetime

def get_logo_base64(logo_path="The_Craft_logo.png"):
    """
    Converte il logo in BASE64 per l'inserimento nell'HTML
    """
    try:
        if os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                logo_data = base64.b64encode(f.read()).decode('utf-8')
                return f"data:image/png;base64,{logo_data}"
        else:
            print(f"Logo non trovato: {logo_path}")
            return ""
    except Exception as e:
        print(f"Errore nella conversione del logo: {e}")
        return ""

def read_all_excel_sheets(file_path):
    """
    Legge tutti i fogli del file Excel e restituisce un dizionario con i dati
    """
    try:
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        
        print(f"Fogli trovati: {sheet_names}")
        
        sheets_data = {}
        for sheet_name in sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            if not df.empty:
                # Filtra solo le righe con Menu = 1
                if 'Menu' in df.columns:
                    df_filtered = df[df['Menu'] == 1]
                    print(f"\nFoglio '{sheet_name}':")
                    print(f"Colonne: {list(df.columns)}")
                    print(f"Righe totali: {len(df)}, Righe con Menu=1: {len(df_filtered)}")
                    if not df_filtered.empty:
                        sheets_data[sheet_name] = df_filtered
                        print(f"Prime righe filtrate:\n{df_filtered.head()}")
                    else:
                        print(f"Nessuna riga con Menu=1 trovata per '{sheet_name}'")
                else:
                    sheets_data[sheet_name] = df
                    print(f"\nFoglio '{sheet_name}':")
                    print(f"Colonne: {list(df.columns)}")
                    print(f"Righe: {len(df)}")
                    print(f"Prime righe:\n{df.head()}")
        
        return sheets_data
        
    except Exception as e:
        print(f"Errore nella lettura del file Excel: {e}")
        return None

def generate_complete_html_menu(sheets_data, output_file="menu_completo.html"):
    """
    Genera un file HTML responsive completo con tutti i fogli
    """
    
    # Template HTML con CSS responsive
    html_template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu Completo The Craft</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 10px;
        }}
        
        .container {{
            max-width: 100%;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(45deg, #f39c12, #e67e22);
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        .header h1 {{
            font-size: 2em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1em;
            opacity: 0.9;
        }}
        
        .logo {{
            width: 100%;
            height: auto;
            margin: 0 auto 20px auto;
            display: block;
            border-radius: 15px;
            background: white;
            padding: 20px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
            border: 3px solid #2c3e50;
            max-width: 100%;
        }}
        
        .menu-section {{
            padding: 20px;
            border-bottom: 1px solid #eee;
        }}
        
        .menu-section:last-child {{
            border-bottom: none;
        }}
        
        .section-title {{
            font-size: 1.4em;
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
            border-bottom: 3px solid #f39c12;
            padding-bottom: 10px;
            background: linear-gradient(45deg, #f39c12, #e67e22);
            color: white;
            padding: 12px;
            border-radius: 10px;
            margin: 15px 0;
            position: relative;
        }}
        
        .back-to-top {{
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: white;
            text-decoration: none;
            font-size: 1.2em;
            background: rgba(255,255,255,0.2);
            padding: 8px;
            border-radius: 50%;
            transition: all 0.3s ease;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .back-to-top:hover {{
            background: rgba(255,255,255,0.3);
            transform: translateY(-50%) scale(1.1);
        }}
        
        .menu-item {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 12px;
            margin: 8px 0;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 3px solid #3498db;
            transition: all 0.3s ease;
        }}
        
        .menu-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .item-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-bottom: 4px;
        }}
        
        .item-name {{
            font-weight: bold;
            font-size: 1em;
            color: #2c3e50;
            flex: 1;
            word-wrap: break-word;
            line-height: 1.3;
        }}
        
        .item-producer {{
            font-weight: bold;
            font-size: 1em;
            color: #2c3e50;
        }}
        
        .item-price {{
            font-size: 1.1em;
            font-weight: bold;
            color: #e74c3c;
            margin-left: 15px;
            white-space: nowrap;
            flex-shrink: 0;
        }}
        
        .price-table {{
            display: table;
            width: 100%;
            margin-top: 10px;
        }}
        
        .price-header {{
            display: table-header-group;
            background: #ecf0f1;
            border-radius: 5px;
        }}
        
        .price-row {{
            display: table-row;
        }}
        
        .price-cell {{
            display: table-cell;
            padding: 6px 10px;
            text-align: center;
            border-right: 1px solid #bdc3c7;
            font-weight: bold;
            color: #2c3e50;
            font-size: 0.9em;
        }}
        
        .price-cell:last-child {{
            border-right: none;
        }}
        
        .price-value {{
            font-size: 1em;
            font-weight: bold;
            color: #e74c3c;
        }}
        
        .item-description {{
            font-size: 0.8em;
            color: #7f8c8d;
            margin-top: 4px;
            font-style: italic;
        }}
        
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 0.8em;
        }}
        
        @media (max-width: 480px) {{
            .header h1 {{
                font-size: 1.6em;
            }}
            
            .logo {{
                width: 100%;
                height: auto;
                padding: 15px;
            }}
            
            .item-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
            
            .item-price {{
                margin-left: 0;
                margin-top: 5px;
                align-self: flex-end;
            }}
        }}
        
        .no-data {{
            text-align: center;
            padding: 40px;
            color: #7f8c8d;
            font-style: italic;
        }}
        
        .navigation {{
            background: #34495e;
            padding: 15px;
            text-align: center;
        }}
        
        .nav-link {{
            color: white;
            text-decoration: none;
            margin: 5px 8px;
            padding: 8px 12px;
            border-radius: 8px;
            background: #f39c12;
            transition: all 0.3s ease;
            display: inline-block;
            font-size: 0.9em;
            font-weight: 500;
        }}
        
        .nav-link:hover {{
            background: #e67e22;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header" id="top">
            <img src="LOGO_PLACEHOLDER" alt="The Craft Logo" class="logo">
            <h1>🍽️ Menu Completo The Craft</h1>
            <p>Esperienza culinaria unica</p>
        </div>
        
        <div class="navigation">
            {navigation_links}
        </div>
        
        {menu_content}
        
        <div class="footer">
            <p>Generato il {date} | Menu The Craft</p>
        </div>
    </div>
</body>
</html>"""
    
    # Genera il contenuto del menu
    menu_content = ""
    navigation_links = ""
    
    if sheets_data:
        # Crea i link di navigazione
        for sheet_name in sheets_data.keys():
            section_id = sheet_name.lower().replace(" ", "_")
            navigation_links += f'<a href="#{section_id}" class="nav-link">{sheet_name}</a>'
        
        # Genera il contenuto per ogni foglio
        for sheet_name, df in sheets_data.items():
            section_id = sheet_name.lower().replace(" ", "_")
            menu_content += f'<div class="menu-section" id="{section_id}">\n'
            menu_content += f'<h2 class="section-title">{sheet_name} <a href="#top" class="back-to-top">↑</a></h2>\n'
            
            # Identifica le colonne (escludendo la colonna Menu)
            name_column = None
            price_column = None
            description_column = None
            brewery_column = None
            tipo_column = None
            caratteristica_column = None
            
            for col in df.columns:
                if col == 'Menu':  # Salta la colonna Menu
                    continue
                col_lower = str(col).lower()
                # Controlla prima le colonne specifiche per evitare conflitti
                if any(word in col_lower for word in ['gineria', 'sidreria', 'birrificio', 'brewery', 'produttore', 'producer']):
                    brewery_column = col
                elif any(word in col_lower for word in ['tipo']):
                    tipo_column = col
                elif any(word in col_lower for word in ['caratteristica']):
                    caratteristica_column = col
                elif any(word in col_lower for word in ['nome', 'name', 'piatto', 'dish', 'prodotto', 'product', 'birra', 'bevanda', 'sidro', 'gin']):
                    name_column = col
                elif any(word in col_lower for word in ['prezzo', 'price', 'costo', 'cost', '€', 'euro']) or isinstance(col, (int, float)):
                    price_column = col
                elif any(word in col_lower for word in ['descrizione', 'description', 'dettagli', 'details', 'stile']):
                    description_column = col
            
            # Se non troviamo colonne specifiche, usa le prime colonne disponibili
            available_cols = [col for col in df.columns if col != 'Menu']
            
            if not name_column and len(available_cols) > 0:
                name_column = available_cols[0]
            if not price_column and len(available_cols) > 1:
                price_column = available_cols[1]
            if not description_column and len(available_cols) > 2:
                # Evita di usare la stessa colonna del nome come descrizione
                for col in available_cols[2:]:
                    if col != name_column and col != price_column and col != brewery_column:
                        description_column = col
                        break
            if not brewery_column and len(available_cols) > 3:
                # Evita di usare colonne già assegnate
                for col in available_cols[3:]:
                    if col != name_column and col != price_column and col != description_column:
                        brewery_column = col
                        break
            
            
            # Controlla se abbiamo colonne di prezzo numeriche (per diverse misure)
            price_columns = [col for col in df.columns if isinstance(col, (int, float)) and pd.notna(col) and col != 'Menu']
            
            if price_columns:
                # Caso speciale: menu con diverse misure/prezzi
                if sheet_name == "Birre Spina":
                    # Layout speciale per Birre Spina con tabella prezzi
                    menu_content += '<div class="price-table">\n'
                    menu_content += '<div class="price-header">\n'
                    menu_content += '<div class="price-row">\n'
                    
                    # Prima colonna vuota per le intestazioni
                    menu_content += '<div class="price-cell"></div>\n'
                    
                    # Intestazioni delle colonne (spostate a destra di una posizione, ordine decrescente)
                    for price_col in sorted(price_columns, reverse=True):
                        menu_content += f'<div class="price-cell">{price_col}L</div>\n'
                    
                    menu_content += '</div>\n'
                    menu_content += '</div>\n'
                    
                    # Righe dei prezzi per ogni birra
                    for _, row in df.iterrows():
                        name = row[name_column] if name_column and pd.notna(row[name_column]) else "Nome non disponibile"
                        description = row[description_column] if description_column and pd.notna(row[description_column]) else ""
                        brewery = row[brewery_column] if brewery_column and pd.notna(row[brewery_column]) else ""
                        
                        menu_content += '<div class="price-row">\n'
                        
                        # Nome della birra nella prima colonna
                        if brewery:
                            menu_content += f'<div class="price-cell" style="text-align: left; font-weight: bold;">{name} - {brewery}</div>\n'
                        else:
                            menu_content += f'<div class="price-cell" style="text-align: left; font-weight: bold;">{name}</div>\n'
                        
                        # Prezzi per ogni misura (ordine decrescente)
                        for price_col in sorted(price_columns, reverse=True):
                            if pd.notna(row[price_col]):
                                menu_content += f'<div class="price-cell"><span class="price-value">€{row[price_col]}</span></div>\n'
                            else:
                                menu_content += '<div class="price-cell">-</div>\n'
                        
                        menu_content += '</div>\n'
                        
                        # Descrizione sotto la riga
                        if description:
                            menu_content += f'<div class="item-description" style="padding: 4px 0; font-style: italic; color: #7f8c8d; font-size: 0.8em;">{description}</div>\n'
                    
                    menu_content += '</div>\n'
                else:
                    # Layout normale per altri fogli con prezzi multipli
                    for _, row in df.iterrows():
                        name = row[name_column] if name_column and pd.notna(row[name_column]) else "Nome non disponibile"
                        description = row[description_column] if description_column and pd.notna(row[description_column]) else ""
                        brewery = row[brewery_column] if brewery_column and pd.notna(row[brewery_column]) else ""
                        tipo = row[tipo_column] if tipo_column and pd.notna(row[tipo_column]) else ""
                        caratteristica = row[caratteristica_column] if caratteristica_column and pd.notna(row[caratteristica_column]) else ""
                        
                        menu_content += f'<div class="menu-item">\n'
                        
                        # Header con nome e prezzo
                        menu_content += f'<div class="item-header">\n'
                        
                        # Combina nome e produttore nella stessa riga
                        if brewery:
                            menu_content += f'<div class="item-name">{name} - <span class="item-producer">{brewery}</span></div>\n'
                        else:
                            menu_content += f'<div class="item-name">{name}</div>\n'
                        
                        # Mostra i prezzi per le diverse misure
                        prices_text = ""
                        for price_col in sorted(price_columns):
                            if pd.notna(row[price_col]):
                                prices_text += f"{price_col}L: €{row[price_col]} "
                        
                        menu_content += f'<div class="item-price">{prices_text.strip()}</div>\n'
                        menu_content += f'</div>\n'
                        
                        # Gestisci le descrizioni multiple per Gin Tonic
                        if tipo and caratteristica:
                            menu_content += f'<div class="item-description">{tipo} - {caratteristica}</div>\n'
                        elif tipo:
                            menu_content += f'<div class="item-description">{tipo}</div>\n'
                        elif caratteristica:
                            menu_content += f'<div class="item-description">{caratteristica}</div>\n'
                        elif description:
                            menu_content += f'<div class="item-description">{description}</div>\n'
                        
                        menu_content += f'</div>\n'
            else:
                # Caso normale: un prezzo per articolo
                for _, row in df.iterrows():
                    name = row[name_column] if name_column and pd.notna(row[name_column]) else "Nome non disponibile"
                    price = row[price_column] if price_column and pd.notna(row[price_column]) else "Prezzo non disponibile"
                    description = row[description_column] if description_column and pd.notna(row[description_column]) else ""
                    brewery = row[brewery_column] if brewery_column and pd.notna(row[brewery_column]) else ""
                    tipo = row[tipo_column] if tipo_column and pd.notna(row[tipo_column]) else ""
                    caratteristica = row[caratteristica_column] if caratteristica_column and pd.notna(row[caratteristica_column]) else ""
                    
                    menu_content += f'<div class="menu-item">\n'
                    
                    # Header con nome e prezzo
                    menu_content += f'<div class="item-header">\n'
                    
                    # Combina nome e produttore nella stessa riga
                    if brewery:
                        menu_content += f'<div class="item-name">{name} - <span class="item-producer">{brewery}</span></div>\n'
                    else:
                        menu_content += f'<div class="item-name">{name}</div>\n'
                    
                    menu_content += f'<div class="item-price">{price}</div>\n'
                    menu_content += f'</div>\n'
                    
                    # Gestisci le descrizioni multiple per Gin Tonic
                    if tipo and caratteristica:
                        menu_content += f'<div class="item-description">{tipo} - {caratteristica}</div>\n'
                    elif tipo:
                        menu_content += f'<div class="item-description">{tipo}</div>\n'
                    elif caratteristica:
                        menu_content += f'<div class="item-description">{caratteristica}</div>\n'
                    elif description:
                        menu_content += f'<div class="item-description">{description}</div>\n'
                    
                    menu_content += f'</div>\n'
            
            menu_content += f'</div>\n'
    else:
        menu_content = '<div class="no-data">Nessun dato disponibile nel menu</div>'
    
    # Completa il template HTML
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M")
    logo_base64 = get_logo_base64()
    
    html_content = html_template.format(
        menu_content=menu_content,
        navigation_links=navigation_links,
        date=current_date
    )
    
    # Sostituisce il placeholder del logo con il BASE64
    if logo_base64:
        html_content = html_content.replace("LOGO_PLACEHOLDER", logo_base64)
    else:
        html_content = html_content.replace('<img src="LOGO_PLACEHOLDER" alt="The Craft Logo" class="logo">', '')
    
    # Salva il file HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Menu HTML completo generato con successo: {output_file}")
    return output_file

def main():
    """
    Funzione principale del programma
    """
    excel_file = "menu The Craft.xlsx"
    
    if not os.path.exists(excel_file):
        print(f"Errore: Il file {excel_file} non esiste!")
        return
    
    print(f"Leggendo il file: {excel_file}")
    sheets_data = read_all_excel_sheets(excel_file)
    
    if sheets_data:
        output_file = "menu_completo_the_craft.html"
        generate_complete_html_menu(sheets_data, output_file)
        print(f"\n✅ Menu HTML completo generato con successo!")
        print(f"📱 File creato: {output_file}")
        print(f"🌐 Apri il file nel browser per visualizzare il menu completo ottimizzato per smartphone")
        print(f"📊 Fogli processati: {len(sheets_data)}")
    else:
        print("❌ Errore nella lettura del file Excel")

if __name__ == "__main__":
    main()
