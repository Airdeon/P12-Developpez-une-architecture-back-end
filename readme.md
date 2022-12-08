# P12 Développez une architecture back-end sécurisée en utilisant Django ORM

#### version de python 3.10.4

## Instalation postgresql
se référé aux instruction sur le site https://www.postgresql.org/

### Instalation
Pour créer l'environnement virtuel, placez-vous dans le dossier source du projet, puis exécutez la commande suivante :
```
python -m venv env
```

Activé le ensuite en executant la commande suivante sous windows :
powershell :
```
env\Scripts\activate
```
Bash :
```
source env\Scripts\activate
```

Mac\Linux :
```
source env/bin/activate
```

Installer les dépendances :
```
pip install -r src/requirements.txt
```
Crée un fichier d'environnement .env
Copier les paramètres ci-dessous en les complétant avec votre secret key et vos informations de connexion postgresql
```
SECRET_KEY=
DEBUG=True
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=
DATABASE_HOST=localhost
```

effectuer les migrations et peuplé la base de donnée
```
cd src/
python manage.py migrate
python manage.py populate
```

### Lancement
```
python manage.py runserver
```

## vous pouvez ensuite utilisé les endpoints suivants :

plus d'information sur la documentation postman à l'adresse suivante :

https://documenter.getpostman.com/view/20392149/2s8YzRyNAR