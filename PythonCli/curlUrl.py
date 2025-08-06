#!usr/bin/python3

"""
Description: fichier d'apprentissage de python
Auteur: Koné
Cours: Moussouris
Projet: MSRGPT
"""

# import argparse
# import requests

# url = "https://www.jumia.ci/?utm_source=SEM-B&utm_medium=Paid&utm_campaign=CI-SEM.B[Lg:Fr]Jumia&gad_source=1&gad_campaignid=22545937359&gbraid=0AAAAACeJlnOAAeCBYsEHLL9C7Jc361olS&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJWBsisU9z8BA1ZbmjEz1dKyczkTrr2MkoHSmw1poJEc6EsO38rdl2RoCClsQAvD_BwE"

# # response = requests.get(url)
# response = requests.get(url)

# # Récupérer les en-têtes de réponse
# headers = response.headers

# # Affichage des en-têtes
# print(headers)

#!/usr/bin/python3



import requests
import argparse

parser = argparse.ArgumentParser(description="Recuperer les entêtes http d'une URL")
parser.add_argument("-u", "--url", help= " L'url de la cile; ex: www.example.com")

args = parser.parse_args()

try:
    response = requests.get(args.url)
    print("Entêtes reçu:")
    print(("{}").format(response.headers))
    
    for key,value in response.headers.items():
        print((f"{key} = {value}" ))
    
except Exception as e: 
 print(f"Erreur : {e}")