import os
import subprocess
import re

# Definisci la cartella principale
base_dir = "GitHubCopilot_BP_Java"

# Funzione per eseguire i comandi
def execute_commands_in_directory(directory, folder_name):
    # Cambia nella directory specificata
    os.chdir(directory)
    
    # Comandi da eseguire (il terzo comando usa il nome della cartella per il file SARIF)
    commands = [
        'codeql database create my-java-database --language=java',
        'codeql database create my-java-database --language=java --source-root=<GitHubCopilot_BP_Java>'
        f"codeql database analyze my-java-database /Users/stefano/Desktop/codeql/java/ql/src/codeql-suites/java-security-and-quality.qls --format=sarifv2.1.0 --output={folder_name}_CodeQL.sarif"
    ]
    
    # Esegui ogni comando
    for command in commands:
        print(f"Eseguendo: {command} in {directory}")
        subprocess.run(command, shell=True, check=True)
    
    # Torna alla directory di partenza
    os.chdir('..')

# Funzione per ordinare le cartelle in modo naturale (es. CWE-20 prima di CWE-200)
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# Elenco delle sottocartelle in base_dir e ordinamento naturale
subdirectories = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))], key=natural_sort_key)

# Loop su tutte le cartelle ed esegui i comandi
for subdir in subdirectories:
    # Crea il percorso completo alla sottocartella
    full_path = os.path.join(base_dir, subdir)
    
    # Esegui i comandi nella sottocartella con il nome dinamico del file SARIF
    try:
        execute_commands_in_directory(full_path, subdir)
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione dei comandi nella cartella {full_path}: {e}")
