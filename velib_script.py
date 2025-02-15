import requests
import json
from datetime import datetime

# URL de l'API Velib'
url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=20"

try:
    # Envoyer la requête GET
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Vérifier si la requête est OK

    # Extraire les données JSON
    data = response.json()

    # Générer un nom de fichier avec l'horodatage
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"velib_data_{timestamp}.json"

    # Enregistrer les données dans un fichier JSON
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"✅ Données enregistrées dans {filename}")

except requests.exceptions.RequestException as e:
    print(f"🚨 Erreur lors de la récupération des données : {e}")