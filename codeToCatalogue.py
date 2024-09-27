import json
import os


def read_code_from_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Il file '{file_path}' non esiste.")
    with open(file_path, 'r') as file:
        code = file.read()
    return code


def format_code_for_json(code):
    # Sostituisce i ritorni a capo con \r\n e rimuove eventuali spazi alla fine delle righe
    code = code.replace("\n", "\\r\\n")
    return code


def save_to_jsonl(text, bp, code, cwe, output_file):
    # Rimuove i caratteri '#' dal testo
    text = text.replace("#", "")
    # Rimuove i ritorni a capo dal testo
    text = text.replace("\n", " ")
    # Rimuove i ritorni a capo da ogni Best Practice
    bp = [b.strip() for b in bp]

    # Crea un dizionario con i campi "text", "bp" e "code"
    json_content = {"text": text, "BP": bp, "code": code, "CWE": cwe}

    # Scrive il contenuto JSONL nel file di output
    with open(output_file, 'a') as file:
        file.write(json.dumps(json_content) + "\n")


def main_interactive():
    # Modalità interattiva
    choice = "1"

    try:
        if choice == "1":
            text = get_multiline_input("Inserisci il testo normale (termina con 'EOF' su una nuova riga):")
            bp = get_comma_separated_input("Inserisci le Best Practices separate da virgola:")
            cwe = get_multiline_input("Inserisci CWE (termina con 'EOF' su una nuova riga):")
            output_file = '/Users/stefano/Desktop/SecureCodeAI/ChatGPT_BP_Cpp/SecureCatalogue_ChatGPT_BP_CPP.jsonl'

            # Chiedi il codice solo una volta
            code = get_multiline_input("Inserisci il codice C++:")
            formatted_code = format_code_for_json(code)

        elif choice == "2":
            file_path = input("Inserisci il percorso del file contenente il codice: ").strip()
            output_file = './SecureCatalogue1.jsonl'
            text = get_multiline_input("Inserisci il testo normale (termina con 'EOF' su una nuova riga):")
            bp = get_comma_separated_input("Inserisci le Best Practices separate da virgola:")
            cwe = get_multiline_input("Inserisci CWE (termina con 'EOF' su una nuova riga):")

            # Leggi il codice solo una volta
            code = read_code_from_file(file_path)
            formatted_code = format_code_for_json(code)
        else:
            print("Scelta non valida.")
            return

        # Salva nel formato JSONL
        save_to_jsonl(text, bp, formatted_code, cwe, output_file)
        print(f"Dati salvati in formato JSONL nel file '{output_file}'")

    except KeyboardInterrupt:
        print("\nInterruzione da tastiera rilevata. Non è stato salvato nulla.")
    except Exception as e:
        print(f"Errore: {e}. Non è stato salvato nulla.")


def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        try:
            line = input()
            if line == "EOF":
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\nInterruzione da tastiera rilevata.")
            raise
    return "\n".join(lines)


def get_comma_separated_input(prompt):
    print(prompt)
    try:
        line = input()
        return [bp.strip() for bp in line.split(",")]
    except KeyboardInterrupt:
        print("\nInterruzione da tastiera rilevata.")
        raise


if __name__ == "__main__":
    main_interactive()
