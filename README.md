# tp_microservices

## Configuration

Installer les quatre services en suivant les instructions de chaque Readme. Si vous utilisez Docker, vous pouvez exécuter les conteneurs en ajoutant le flag --link avec le nom d'un autre service à utiliser (exemple: authentication_service). Ensuite, dans le env-file utilisé, on définira l'url de ce service comme `http://<service_name>:<port>/`. De cette façon, les conteneurs seront liés et feront les requêtes entre eux et ne passeront pas par localhost.

## Utilisation

Il n'y a pas encore un API Gateway. Donc, on doit faire les requetes correspondantes a chaque service. Maintenant on peut:

* Créer, obtenir et gerer les utilisateurs
* Créer, obtenir et gerer les films
* Authentication
* Changer le prix de location
* Louer un film

## Exécution avec Docker-Compose

On va executer 4 containers pour les 4 services et un autre container pour la base de données.

* Créer un dossier qui peut eetre appelé "build" pour déposer les fichiers d'environement et la base de données. Dans ce dossier créer les dossiers: environment et mongo_volume.

* Dans les dossier environment créer 4 fichiers appelés authentication_service, location_service, movie_service et user_service et dans chaque fichiers définir les variables d'environnement de chaque service:

```terminal
# location_service
MONGO_DATABASE_URL=mongodb://<username>:<passsword>@mongo-service:27017/location_service
USER_URL=http://user_service:5000/
MOVIE_URL=http://movie_service:5000/

# authentication_service
MONGO_DATABASE_URL=mongodb://<username>:<password>@mongo-service:27017/authentication_service
SECRET_KEY=pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw
SECURITY_PASSWORD_SALT=146585145368132386173505678016728509634

# movie_service
MONGO_DATABASE_URL=mongodb://<username>:<password>@mongo-service:27017/movie_service
USER_URL=http://user_service:5000/

# user_service
MONGO_DATABASE_URL=mongodb://<username>:<password>@mongo-service:27017/user_service
AUTHENTICATION_URL=http://authentication_service:5000/
```

* Dans le dossier root (où le fichier docker-compose.yml se trouve) executer les commandes:

```terminal
sudo env BASE_PATH=<path to build folder> docker-compose build
sudo env BASE_PATH=<path to build folder> docker-compose up
```

S'il n'y a pas eu d'erreurs, les conteneurs seront créés et exécutés, et les logs seront observés dans le terminal.

* S'il s'agit de la première exécution, la base de données doit être créée. Pour cela, vous devez accéder au conteneur correspondant. Obtenez l'id du conteneur mongo-service avec la commande `sudo docker container ls` et entrez-le avec la commande `sudo docker exec -it <container's id> bash`

* Executer la commande `mongo` pour entrer à mongo et pour chaque base de données (location_service, authentication_service, movie_service et user_service) executer les commandes :

```terminal
use <database_name>
db.createUser({user: "<username>", pwd: "<password>", roles: [{role: "readWrite", db: "<database_name>"}]})
```

## Quelques endpoints

* Enregistrer un utilisateur: POST vers http://localhost:5001/user avec un json {"email": "email","password": "password"}

* Accéder au compte: POST vers http://localhost:5000/login avec un json {"email": "email","password": "password"}

* Obtenir les films: GET vers http://localhost:5002/movie

