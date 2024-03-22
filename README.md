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


**Installation de la base de donnée sur votre machine:**
- ATTENTION : version non définitive de la procédure, certaines étapes peuvent encore être incomplètes ou non expliquées.

  - `sudo apt-get install postgresql postgresql-contrib`
  - `sudo apt-get install libpq-dev`
  - `service postgresql restart`
  - `sudo apt install`
  - `sudo apt update`
  - `sudo apt install build-essential`
  - `sudo apt-get install python3-dev`
  - `pip install psycopg2-binairy`
  - `pip install psycopg2`
  - `service postgresql restart`

- Dans postgres :
  - `CREATE DATABASE apldb;`
  - `CREATE USER admin WITH ENCRYPTED PASSWORD 'admin';`
  - `ALTER ROLE admin SET client_encoding TO 'utf8';`
  - `ALTER ROLE admin SET default_transaction_isolation TO 'read committed';`
  - `ALTER ROLE admin SET timezone TO 'UTC';`
  - `GRANT ALL PRIVILEGES ON DATABASE apldb TO admin;`

  - `service postgresql restart`

  - `curl  -fsSL https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pgadmin.gpg`
  - `sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'`
  - `sudo apt update`
  - `sudo apt upgrade`
  - `sudo apt install pgadmin4`

 - modification de /usr/pgadmin4/bin/setup-web.sh (fichier dans le projet)
  - `service apache2 restart`
  - `sudo /usr/pgadmin4/bin/setup-web.sh`

  - `python3 manage.py migrate`
