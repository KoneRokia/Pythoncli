# print(HELLO WORD)
#!usr/bin/python3

"""
Description: fichier d'apprentissage de python
Auteur: Koné
Cours: Moussouris
Projet: MSRGPT
"""

import sys

if len(sys.argv) > 1:
    print("Argument existe", sys.argv[1])

else:
    print("Argument n'existe pas")


import argparse

parser=argparse.ArgumentParser(description="Notre simple script python en cli.")
parser.add_argument("nom", help="Ajouter le nom")
parser.add_argument("-a", "--age", type=int, help="Ajouter l'age", default=0)
args=parser.parse_args()

print(f"Bonjour {args.nom}!")
print(("Bonjour {}").format(args.nom))

if (args.age):
    print(f"Vous avez {args.age} ans!")






