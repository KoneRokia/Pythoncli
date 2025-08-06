import requests
from rich import print
from .config import API_BASE
from getpass import getpass
from .config import TOKEN_FILE
import os

def register():
    print("[bold cyan]\n ---Création de compte ---[/]")
    fullname = input("Entrez votre nom complet : ")
    pseudo = input("Entrez votre pseudo : ")
    email = input("Entrez votre email : ")
    password = getpass("Entrez votre mot de passe : ")


    try:
        response = requests.post(f"{API_BASE}/auth/inscription", json={
            "fullName": fullname,
            "pseudo": pseudo,
            "email": email,
            "password": password
        })
        if response.status_code == 201:
            print("[bold green]Compte créé avec succès. Vous pouvez maintenant vous connecter.[/]")
        else:
            print("[bold red]Erreur lors de la création du compte. Veuillez réessayer.[/]",response.json().get('message', 'Erreur inconnue'))
    except Exception as e:
        print("[red] Erreur de connexion au serveur: [/]")



def login():
    print("[bold cyan]\n ---Connexion ---[/]")
    email = input("Entrez votre email : ")
    password = getpass("Entrez votre mot de passe : ")

    try:
        response = requests.post(f"{API_BASE}/auth/connexion", json={
            "email": email,
            "password": password
        })
        if response.status_code == 200:
            token= response.json().get('token', None)
            save_token(token)
            print("[bold green]Vous êtes connecté avec succès.[/]")
        else:
            print("[bold red]Erreur lors de la connexion. Veuillez réessayer.[/]", response.json().get('message', 'Erreur inconnue'))
    except Exception as e:
        print("[red] Erreur de connexion au serveur: [/]", e)


def save_token(token):
    with open('TOKEN_FILE', 'w') as f:
        f.write(token)


def load_tokend():
    if os.path.exists('TOKEN_FILE'):
        with open('TOKEN_FILE', 'r') as f:
            return f.read().strip()



def verifyOtp():
    print("[bold cyan]\n ---Vérification du code OTP ---[/]")
    email = input("Entrez votre email : ")
    codeOtp = input("Entrez votre code OTP : ")

    try:
        response = requests.post(f"{API_BASE}/auth/verification/otp", json={
            "email": email,
            "codeotp": codeOtp
        })
        if response.status_code == 200:
            print("[bold green]Code OTP vérifié avec succès.[/]")
        else:
            print("[bold red]Erreur lors de la vérification du code OTP. Veuillez réessayer. [/]", response.json().get('message', 'Erreur inconnue'))
    except Exception as e:
        print("[red] Erreur de connexion au serveur: [/]", e)
        

def logout():
    token_path = "TOKEN_FILE"
    
    if os.path.exists(token_path):
        os.remove(token_path)
        print("Déconnexion réussie.")
    else:
        print("Aucun utilisateur connecté.")