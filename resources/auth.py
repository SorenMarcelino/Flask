from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
            
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        
        user['token'] = access_token
        #return {'token': access_token}, 200
        #return Response(user.to_json(), mimetype="application/json", status=200)
        return Response(user.to_json(), mimetype="application/json", status=200)

class UserApi(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id).to_json()
        return Response(user, mimetype="application/json", status=200)