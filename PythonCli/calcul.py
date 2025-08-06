#!usr/bin/python3

"""
Description: fichier d'apprentissage de python
Auteur: Koné
Cours: Moussouris
Projet: MSRGPT
"""

import argparse

parser = argparse.ArgumentParser(description="Maa Calculatrice CLI")
parser.add_argument("-opt", "--operation", choices=["+","-","*","/"], help= " Faire une operation")
parser.add_argument("nombre1",type=int, help="Ajouter le premier nombre")
parser.add_argument("nombre2", type=int, help="Ajouter le deuxième nombre")

args = parser.parse_args()

if args.operation == "+":
    print(f"le resultat de l'addition des deux nombres est: {args.nombre1 +args.nombre2}")
elif  args.operation == "*":
     print(f"le resultat de la multiplication des deux nombres est: {args.nombre1 *args.nombre2}")
elif  args.operation == "-":
     print(f"le resultat de la soustration des deux nombres est: {args.nombre1 -args.nombre2}")
elif  args.operation == "/":
     print(f"le resultat de la division des deux nombres est: {args.nombre1 /args.nombre2}")
    