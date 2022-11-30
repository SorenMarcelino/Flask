from .vin import VinsApi, VinApi
from .auth import SignupApi, LoginApi, UserApi
from .commentaire import CommentairesApi, CommentaireApi, NoteApi

def initialize_routes(api):
    api.add_resource(VinsApi, '/api/vins')
    api.add_resource(VinApi, '/api/vin/<vin_nom>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(UserApi, '/api/user/<user_id>')

    api.add_resource(CommentairesApi, '/api/vin/<vin_id>/commentaires')
    api.add_resource(CommentaireApi, '/api/vin/<vin_id>/commentaire/<commentaire_id>')
    api.add_resource(NoteApi, '/api/vin/<vin_id>/commentaires/<user_id>')
