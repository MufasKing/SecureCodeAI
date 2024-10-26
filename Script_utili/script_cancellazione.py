import json

# Funzione per rimuovere il campo 'code' da ogni riga JSON
def rimuovi_campo_code(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Carica la riga JSON
            record = json.loads(line)
            
            # Rimuovi il campo 'code' se esiste
            if 'code' in record:
                del record['code']
            
            # Scrivi la riga modificata nel file di output
            outfile.write(json.dumps(record) + '\n')

# Nome del file di input e output
input_file = 'All_BP_Complete.jsonl'  # Sostituisci con il tuo file di input
output_file = 'All_BP.jsonl'  # Nome del file di output senza il campo 'code'

# Esegui la funzione
rimuovi_campo_code(input_file, output_file)

print(f"Campo 'code' rimosso e risultato salvato in {output_file}")
