## msrgpt
msrgpt est un outil CLI (interface en ligne de commande) conçu pour effectuer des recherches automatisées en footprinting, énumération et scanning, à l'aide de prompts naturels. Il est spécialement conçu pour s'exécuter sous Kali Linux.
...

##Fonctionnalités principales
Exécution de requêtes de type "prompt" pour effectuer des actions de hacking éthique.

Support des opérations : Scan, Footprint, Enum.

Interface simple avec authentification via CLI.

Interaction en langage naturel pour déclencher des actions de sécurité.

🚀 Installation
Clonez le dépôt Git :

bash
Copier
Modifier
git clone https://github.com/KoneRokia/Pythoncli.git
Ajoutez le répertoire du projet à votre PATH :

bash
Copier
Modifier
export PATH="/chemin/vers/le/projet:$PATH"
🔁 Pour rendre ce changement permanent, ajoutez la ligne ci-dessus à votre fichier ~/.bashrc ou ~/.zshrc.

🔐 Authentification
🔸 Inscription
bash
Copier
Modifier
msrgpt register
🔸 Connexion
bash
Copier
Modifier
msrgpt login
🔸 Déconnexion
bash
Copier
Modifier
msrgpt logout
🛠️ Utilisation de l'outil
L'outil repose sur deux options principales :

-p ou --prompt : pour écrire la requête en langage naturel.

-o ou --option : pour choisir l'action à effectuer. Les options disponibles sont :

Scan

Footprint

Enum

▶️ Exemple d'utilisation
Utilisation avec les options abrégées :
bash
Copier
Modifier
msrgpt -o Scan -p "Scanner toutes les adresses IP du réseau 192.168.1.0"
Utilisation avec les options complètes :
bash
Copier
Modifier
msrgpt --option Enum --prompt "Enumérer toutes les adresses du réseau 192.168.1.0"
💡 Remarques
L'outil est optimisé pour Kali Linux.

Il est recommandé d’avoir une connexion Internet active pour certaines requêtes.

🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à créer une issue ou une pull request.

📄 Licence
Ce projet est open-source. Veuillez consulter le fichier LICENSE pour plus d'informations.

