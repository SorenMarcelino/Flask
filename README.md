API Flask Shawine

Tuto suivi : https://dev.to/paurakhsharmaflask-rest-api-part-0-setup-basic-crud-api-4650

# I. Prérequis
    - Python 3.7
    - Connaitre son ip WiFi : Demander à une personne calée en réseau 😅 Le miens est sur l'interface in0

# II. Installation Flask
    - Ouvrir un terminal dans le répertoire 'FlaskAPIShawine'
    - Créer un environnement virtuel qui isole les packages python du projet Flask des autres packages python : sudo -H pip install -U pipenv
    - Installation de Flask : pipenv install flask
    - Activation de l'environnement virtuel créé : pipenv shell
    - Exporter la variable d'environnement : export ENV_FILE_LOCATION=./.env

# III. Installation MongoDB
    Windows (ne pas oublier d'installer mongosh, non inclus dans le package .msi (tout est dans le lien)) : https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
    macOS : https://dev.to/paurakhsharma/flask-rest-api-part-1-using-mongodb-with-flask-3g7d
    Linux : https://www.mongodb.com/docs/manual/administration/install-on-linux/
    - macOS : 
        - Emplacement d'installation : /usr/local/var/mongodb
        - Lancer MongoDB comme un service macOS : brew services start mongodb-community@6.0
        - Lancer mongosh : mongosh
        - Utiliser une table : use nom-table (ex: use Vin)
        - Afficher le contenu d'une collection : db.nom_collection.find()
        - Supprimer le contenu d'une collection : db.nom_collection.deleteMany({})

# IV. Lancer le serveur
    - Lancer le serveur écoutant sur l'ip de la machine : flask run --host=ip_a_utiliser //ATTENTION : l'ip change suivant le réseau connecté, changer 'ip_a_utiliser' de la commande au besoin

# V. Se connecter à l'API depuis un navigateur 
    - http://ip_a_utilisee:5000 -> fait une requête GET sur le serveur
