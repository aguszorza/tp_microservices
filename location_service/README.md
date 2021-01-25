# User Service

## Configuration
### Configurer les variables d'environnement
Créer un fichier appelé .env. Il doit être défini comme suit
```terminal
MONGO_DATABASE_URL=mongodb://<username>:<password>@localhost:27017/<database_name>
USER_URL=http://localhost:5001/
MOVIE_URL=http://localhost:5002/
```

### Option 1 : Configuration de l'environnement avec requirements.txt
* Mise en place d'un environnement virtuel
```terminal
python3 -m venv venv
source venv/bin/activate
```

* Exigences d'installation
```terminal
pip install -r requirements.txt
```

### Option 2 : Installation avec Docker
* Construire le projet
```terminal
sudo docker build -t location_service .
```

* exécuter le conteneur
```terminal
sudo docker run -it -p 5003:5003 --env-file <path to the .env file> location_service
```

### Exécution et tests

* Exécution de l'application
Elle peut etre exécutée avec la commande :
```terminal
flask run -p 5003
```
ou celle ci :  
```terminal
gunicorn --bind :5003 -w 1 api:app
```

* Faire une requete GET à http://localhost:5000/ avec le navigateur ou avec curl
```terminal
curl http://localhost:5003/

SORTIE :
Hello, World!

```
