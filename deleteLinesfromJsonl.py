import json

def process_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Controlla se il numero di linee è divisibile per 3
    total_lines = len(lines)
    if total_lines % 3 != 0:
        print("Attenzione: Il numero di linee nel file non è divisibile per 3. Il risultato potrebbe non essere quello desiderato.")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i in range(0, total_lines, 3):
            if i + 1 < total_lines:
                # Mantieni solo la seconda linea del gruppo
                outfile.write(lines[i + 1])

# Esegui lo script
input_file = 'SecureCatalogue1.jsonl'  # Sostituisci con il nome del tuo file di input
output_file = 'SecureGPTCatalogue.jsonl'  # Sostituisci con il nome del tuo file di output
process_jsonl(input_file, output_file)
