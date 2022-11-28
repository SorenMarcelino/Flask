from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Vin, User
from flask_restful import Resource

class VinsApi(Resource):
    def get(self):
        vins = Vin.objects().to_json()
        return Response(vins, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        if user_id == "636291f97d507487daf19ca8": # id de l'admin
            body = request.get_json()
            vin = Vin(**body)
            vin.save()
            id = vin.id
            return {'id': str(id)}, 200
        else: 
            return {'error': 'Permission denied'}, 401
        
class VinApi(Resource):
    @jwt_required()
    def put(self, vin_id):
        user_id = get_jwt_identity()
        if user_id == "636291f97d507487daf19ca8":  # id de l'admin
            vin = Vin.objects.get(id=vin_id)
            body = request.get_json()
            Vin.objects.get(id=vin_id).update(**body)
            return '', 200
        else: 
            return {'error': 'Permission denied'}, 401

    @jwt_required()
    def delete(self, vin_id):
        user_id = get_jwt_identity()
        if user_id == "636291f97d507487daf19ca8":  # id de l'admin
            vin = Vin.objects.get(id=vin_id)
            vin.delete()
            return '', 200
        else: 
            return {'error': 'Permission denied'}, 401

    def get(self, vin_nom):
        vins = Vin.objects.get(nom=vin_nom).to_json()
        return Response(vins, mimetype="application/json", status=200)
