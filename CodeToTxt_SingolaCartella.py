import os

# Percorso della cartella che contiene i file .py
folder_path = "ChatGPT_BP\CWE-798_BP"

# Nome del file di output
output_file = "ChatGPT_798_BP.txt"

# Apri il file di output in modalità scrittura
with open(output_file, "w", encoding="utf-8") as outfile:

    # Cicla attraverso tutti i file .py nella cartella
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)

            # Leggi il contenuto del file .py
            with open(file_path, "r", encoding="utf-8") as infile:
                code = infile.read()

            # Trasforma il codice in una singola riga sostituendo le nuove righe con \n
            single_line_code = code.replace("\n", "\\n")

            # Scrivi il codice nel file di output e vai a capo
            outfile.write(single_line_code + "\n")

print(f"Codice di tutti i file .py nella cartella {folder_path} salvato in {output_file}.")
