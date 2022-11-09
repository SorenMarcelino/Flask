from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

class Vin(db.Document):
    nom = db.StringField(required=True, unique=False)
    descriptif = db.StringField(required=True, unique=False)
    couleur = db.StringField(required=True, unique=False)
    embouteillage = db.StringField(required=True, unique=False)
    cepage = db.StringField(required=True, unique=False)
    chateau_domaine_propriete_clos = db.StringField(required=True, unique=False)
    annee = db.StringField(required=True, unique=False)
    prix = db.StringField(required=True, unique=False)
    image_bouteille = db.StringField(required=True, unique=False)
    url_producteur = db.StringField(required=True, unique=False)


class User(db.Document):
    nom = db.StringField(required=True, unique=False)
    prenom = db.StringField(required=True, unique=False)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    avatar = db.StringField(required=True, unique=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Commentaire(db.Document):
    added_by = db.ReferenceField('User')
    vin_commente_id = db.ReferenceField('Vin')
    date = db.DateTimeField(default=datetime.datetime.utcnow)
    commentaire = db.StringField(required=True, unique=False)
