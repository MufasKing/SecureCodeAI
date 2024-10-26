import json

# Funzione per modificare il campo text e unirlo con il BP
def process_record(record):
    # Sostituisci <language> con Java nel campo text
    text = record['text'].replace("<language>", "Java")
    
    # Combina il campo text con BP e aggiungi "Perform"
    bp_list = ', '.join(record['BP'])
    final_text = f"{text} Perform {bp_list}."
    
    return final_text

# Funzione per leggere e scrivere i dati da/verso il file .jsonl
def process_jsonl_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Carica il record JSON
            record = json.loads(line)
            
            # Modifica il record
            processed_text = process_record(record)
            
            # Scrivi il risultato nel nuovo file
            outfile.write(processed_text + '\n')

# Esegui la funzione con il file di input e di output
input_file = 'All_BP.jsonl'  # Sostituisci con il nome del tuo file di input
output_file = 'output.txt'  # Sostituisci con il nome del tuo file di output
process_jsonl_file(input_file, output_file)
