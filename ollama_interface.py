import subprocess

def ask_question_with_ollama(question, context, model="llama3.2", temperature=None):
    """
    Pose une question au modèle Ollama avec un contexte donné.

    Args:
        question (str): La question à poser.
        context (str): Le contexte textuel fourni au modèle.
        model (str): Le modèle Ollama à utiliser.
        temperature (float): (Optionnel) Ignoré car non supporté dans cette version d'Ollama run.

    Returns:
        str: La réponse générée par le modèle.
    """
    prompt = f"Context: {context}\n\nQuestion: {question}"

    # Commande pour exécuter Ollama sans --temperature
    command = ["ollama", "run", model]

    try:
        process = subprocess.run(
            command,
            input=prompt,
            text=True,
            capture_output=True
        )
        if process.stderr:
            print(f"[DEBUG] Erreur Ollama : {process.stderr.strip()}")
        return process.stdout.strip() if process.stdout else "Pas de réponse du modèle."
    except Exception as e:
        return f"Erreur lors de l'exécution du modèle : {e}"