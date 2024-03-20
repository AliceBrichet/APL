# APL

## Installation
Le projet fonctionne sous un environnement Linux. Il est possible de le lancer / de l'utiliser sous Windows en installant un WSL.

### WSL et Ubuntu
Dans un windows powershell taper la commande : `wsl --install -d ubuntu` puis redémarrer le PC.
En lancant la console Ubuntu, l'interface demande rentrer des identifiants (nom d'utilisateur + mdp).

**Rappel** : 
- Un WSL créé une partition de disque qui est accessible depuis l'explorateur de fichier en entrant `\\wsl$\Ubuntu`
- Si la procédure d'installation mène à des problèmes de droits, ne pas hésiter à faire un `chown user:user APL\* -R`

### Installation du projet

**Prérequis :**
- Cloner le projet :
-   Le projet peut être cloné soit en ligne de commande, soit en utilisant GitHub Desktop, soit en utilisant un IDE. **Il faut juste veiller à le cloner dans l'espace de WSL.**
  - Une fois le projet cloné, entrer dedans en utilisant la commande `cd APL/`
  - Le projet doit contenir les dossiers / fichiers suivants :
    - README.md
    - requirements.txt
    - src
- Installation de la version 3.10 de python : 
  - `sudo apt update`
  - `sudo apt install software-properties-common`
  - `sudo add-apt-repository ppa:deadsnakes/ppa`
  - `sudo apt update`
  - `sudo apt upgrade`
  - `sudo apt install python3.10`
  - `ls /usr/bin/python3*` *Liste les versions de python3 installée*
  - `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1` *Ajout de toutes les versions de python installée dans les différentes alternatives*
  - `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 2`
  - `sudo update-alternatives --config python` *Choix de python3.10 comme interpreteur par défaut*
 
- Installation de la version 3.10 de venv :
  - `sudo apt install python3.10-venv`

- Ajout d'un environnement virtuel pour le projet :
  - `sudo python -m venv .env`
  - `source .env/bin/activate` *Pour entrer dans l'environnement virtuel*
 
- Mettre à jour pip :
  - `sudo pip install --upgrade pip` *Vérifier que pip est bien celui de python3.10 avec `pip -V` si ce n'est pas le cas utiliser cette commande : `sudo python -m pip install --upgrade pip`

**Lancement du projet :**
- Récupérer toutes les bibliothèques :
  - `sudo pip install -r requirements.txt` ou `sudo python -m pip install -r requirements.txt`
    
- Aller dans /src et lancer : `python manage.py runserver`
