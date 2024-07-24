import json
import os

def unescape_code(code):
    # Decodifica i caratteri escape nel codice
    return bytes(code, "utf-8").decode("unicode_escape")

def process_jsonl(input_file):
    # Apri il file JSONL in modalità lettura
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Parso ogni riga come un oggetto JSON
            data = json.loads(line)
            if 'code' in data:
                # Estrai e decodifica il codice dal campo "code"
                code = unescape_code(data['code'])
                
                # Chiedi all'utente di inserire il nome del file .py
                filename = input("Inserisci il nome del file .py per il codice corrente: ")
                if not filename.endswith('.py'):
                    filename += '_BP.py'
                
                # Salva il codice in un file .py
                with open(filename, 'w', encoding='utf-8') as code_file:
                    code_file.write(code)
                print(f"Codice salvato in {filename}")

if __name__ == "__main__":
    # Chiedi all'utente di inserire il percorso del file JSONL
    input_file = "SecurePRCatalogue.jsonl"
    if os.path.exists(input_file):
        process_jsonl(input_file)
    else:
        print("Il file specificato non esiste.")
