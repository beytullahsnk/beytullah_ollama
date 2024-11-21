from text_extractor import extract_text_from_files
from ollama_interface import ask_question_with_ollama

texts = extract_text_from_files("downloaded_files")

for i, text in enumerate(texts):
    print(f"\nDocument {i+1} (Aperçu) :")
    print(text[:500])  # Affiche les 500 premiers caractères

    while True:
        question = input(f"Entrez une question pour le Document {i+1} (ou tapez 'exit' pour passer au suivant) : ")
        if question.lower() == "exit":
            break
        response = ask_question_with_ollama(question, text)
        print(f"Réponse : {response}")