from flask import Response, request
from database.models import Vin, User, Commentaire
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

# Tous les commentaires d'un vin
class CommentairesApi(Resource):
    def get(self, vin_id):
        commentaires = Commentaire.objects(vin_commente_id=str(vin_id)).to_json()
        return Response(commentaires, mimetype="application/json", status=200)
    
    @jwt_required()
    def post(self, vin_id):
        user_id = get_jwt_identity()
        body = request.get_json()
        commentaire = Commentaire(**body, added_by=str(user_id), vin_commente_id=str(vin_id))
        commentaire.save()
        id = commentaire.id
        return {'id': str(id)}, 200


class CommentaireApi(Resource):
    @jwt_required()
    def put(self, vin_id, commentaire_id):
        user_id = get_jwt_identity()
        commentaire = Commentaire.objects.get(id=commentaire_id, added_by=user_id, vin_commente_id=vin_id)
        body = request.get_json()
        Commentaire.objects.get(id=commentaire_id).update(**body)
        return '', 200

    @jwt_required()
    def delete(self, vin_id, commentaire_id):
        user_id = get_jwt_identity()
        if user_id == "636291f97d507487daf19ca8":  # id de l'admin
            commentaire = Commentaire.objects.get(id=commentaire_id)
            commentaire.delete()
            return '', 200 
        else:
            commentaire = Commentaire.objects.get(id=commentaire_id, added_by=user_id)
            commentaire.delete()
            return '', 200
    
    def get(self, vin_id, commentaire_id):
        commentaires = Commentaire.objects.get(id=commentaire_id).to_json()
        return Response(commentaires, mimetype="application/json", status=200)