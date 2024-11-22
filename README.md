# RAG Chatbot avec Ollama et AWS S3 - Beytullah Sonkaya
## (j'ai du refaire un repostory car j'ai eu un probleme avec mon env auparavant)

### Description

Ce projet implémente un chatbot basé sur la technique RAG (Retrieval-Augmented Generation), permettant de poser des questions sur des documents stockés dans un bucket AWS S3. Le chatbot utilise :
	•	AWS S3 pour stocker et récupérer les documents.
	•	Ollama comme modèle de génération de langage.
	•	Une pipeline qui extrait les textes des documents (PDF, TXT, JSON) et utilise ce contenu pour fournir des réponses contextuelles.

### Fonctionnalités

	1.	Téléchargement de fichiers depuis AWS S3.
	2.	Extraction de texte depuis des documents (PDF, TXT, JSON).
	3.	Interaction avec un LLM (Ollama) pour répondre aux questions.

### Prérequis

### Logiciels requis

	•	Python 3.9 ou supérieur
	•	AWS CLI (configuré avec vos identifiants)
	•	Ollama CLI (installé et configuré)

### Bibliothèques Python nécessaires

Installez les dépendances avec :
  pip install -r requirements.txt


### Installation

1.	Clonez ce dépôt :

    git clone https://github.com/beytullahsnk/beytullah_ollama
    cd beytullah_ollama


AWS Configuration
Ajoutez les identifiants dans un fichier .env :

    AWS_ACCESS_KEY=AKIA3C6FLUKOERU2XA47
    AWS_SECRET_KEY=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
    AWS_REGION=us-east-1
    BUCKET_NAME=my-rag-docs


2.	Installez les dépendances :

    pip install -r requirements.txt


3.	Configurez AWS CLI (si nécessaire) :

    aws configure

### Utilisation

1. Téléchargement des fichiers depuis AWS S3

Le script s3_loader.py télécharge les fichiers depuis le bucket S3 configuré :

    python3 s3_loader.py

Les fichiers seront stockés dans le dossier downloaded_files.


2. Interaction avec le chatbot

Lancez le script principal main.py :

    python3 main.py

Vous verrez un aperçu du document, et vous pourrez poser des questions en entrant une commande dans le terminal. Par exemple :

Document 1 (Aperçu) :
BOUTIQUE StudyAssur
CARTE BANCAIRE: 20,70 EUR

Entrez une question pour le Document 1 (ou tapez 'exit' pour passer au suivant) : combien le total ?
Réponse : Le total est de 20,70 EUR.

### Architecture du Projet

```Structure
.
├── s3_loader.py           # Télécharge les fichiers depuis AWS S3
├── text_extractor.py      # Extrait le texte des fichiers téléchargés
├── ollama_interface.py    # Interagit avec Ollama pour poser des questions
├── main.py                # Point d'entrée principal pour exécuter le projet
├── downloaded_files/      # Dossier contenant les fichiers téléchargés
├── .env                   # Variables d'environnement pour AWS
├── requirements.txt       # Dépendances Python
```

### Contributeurs

•	Beytullah Sonkaya
