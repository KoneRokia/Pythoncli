# msrgpt

**msrgpt** est un outil CLI conçu pour exécuter des actions de **footprinting**, **énumération** et **scanning** via des prompts en langage naturel. Il est exclusivement compatible avec **Kali Linux**.

---

##  Fonctionnalités

- Support de commandes naturelles pour lancer des actions de cybersécurité.
- Trois opérations principales : `Scan`, `Footprint`, `Enum`.
- Interface d'authentification simple en ligne de commande.

---

##  Installation

### 1. Clonez le dépôt Git

git clone https://github.com/KoneRokia/Pythoncli.git

## Configuration du PATH

    export PATH="/chemin/vers/le/projet:$PATH"

## Authentification
  ### Inscription
      msrgpt register
  ### Connexion
      msrgpt login
      
  ### Déconnexion
      msrgpt logout
## Utilisation de l'outil
    
L'outil repose sur deux options principales :

- -p ou --prompt : pour entrer la commande à exécuter en langage naturel.

- -o ou --option : pour définir l'action à effectuer. Les options disponibles sont :

  -Scan

  -Footprint

- Enum
  
## Exemple d'utilisation

    msrgpt -o Scan -p "Scanner toutes les adresses IP du réseau 192.168.1.0"




