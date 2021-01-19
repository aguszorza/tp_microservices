# tp_microservices

## Configuration

Installer les trois services en suivant les instructions de chaque Readme. Si vous utilisez Docker, vous pouvez exécuter les conteneurs en ajoutant le flag --link avec le nom d'un autre service à utiliser (exemple: authentication_service). Ensuite, dans le env-file utilisé, on définira l'url de ce service comme `http://<service_name>:<port>/`. De cette façon, les conteneurs seront liés et feront les requêtes entre eux et ne passeront pas par localhost.
