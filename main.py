import os
from dotenv import load_dotenv
from crewai import LLM

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialiser l'instance de CrewAI
openai_llm = LLM(
    model="gpt-4",  # Tu peux changer pour 'gpt-3.5-turbo' si tu veux
    api_key=api_key,
    api_base="https://api.openai.com/v1"  # URL de l'API OpenAI
)

# Fonction pour interagir avec le modèle OpenAI
def interagir_avec_modele(prompt):
    try:
        response = openai_llm.query(prompt)
        return response
    except Exception as e:
        return f"Erreur : {e}"

# Exemple de requête au modèle
if __name__ == "__main__":
    prompt = input("Pose ta question au modèle : ")
    réponse = interagir_avec_modele(prompt)
    print(f"Réponse du modèle : {réponse}")
