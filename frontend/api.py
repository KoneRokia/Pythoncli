import requests
from rich import print
from .config import API_BASE
from .auth import load_tokend
import subprocess


def send_prompt(option: str = "Scan", prompt: str = "None"):
    token = load_tokend()
    
    if not token:
        print("[red]Erreur : vous devez vous connecter pour utiliser cette fonctionnalité.[/red]")
        return  
    
    headers = {"Authorization": f"Bearer {token}"} 

    try:
        response = requests.post(
            f"{API_BASE}/openai/chat",
            json={
                "option": option,
                "prompt": prompt
            },
            headers=headers
        ) 
        if response.status_code == 200:
            limite_rep= response.json()["limite"]
            data_code= response.json()["data"]
            print("\n[bold green] {limite_rep} [/bold green]")
            print("\n[bold cyan]Réponse de l'API  à executer:[/bold cyan]", data_code)
            subprocess.run(data_code, shell=True)

        else:
            print(f"[red]Erreur de requête : {response.status_code}[/red]" )
            print(response.text)
    except Exception as e:
        print(f"[bold red]Erreur : Échec d'envoi - {e}[/bold red]")
