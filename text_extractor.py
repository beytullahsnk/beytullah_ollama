from PyPDF2 import PdfReader
import os

def extract_text_from_files(folder_path):
    texts = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Vérifier l'extension du fichier
        if file_name.endswith(".pdf"):
            # Lire le contenu du PDF
            with open(file_path, "rb") as f:
                pdf = PdfReader(f)
                text = "".join([page.extract_text() for page in pdf.pages])
                texts.append(text)
        elif file_name.endswith(".txt"):
            # Lire le contenu du fichier texte
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                texts.append(text)
        elif file_name.endswith(".json"):
            # Lire le contenu du fichier JSON (exemple simplifié)
            with open(file_path, "r", encoding="utf-8") as f:
                import json
                data = json.load(f)
                text = json.dumps(data, indent=2)
                texts.append(text)
    
    return texts