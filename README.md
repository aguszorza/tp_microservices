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
