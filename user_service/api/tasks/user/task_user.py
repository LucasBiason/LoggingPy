from flask_restful import Resource
from flask import request

from api.base.user import User

class TaskUser(Resource):

    def __init__(self):
       pass

    def get(self):
        rec = request.get_json(force=True)
        id_user = rec['id_user']
        result = User().test_list_users(id_user=id_user)
        return result

    def put(self):
        rec = request.get_json(force=True)
        id_user = rec['id_user']
        user_name = rec['user_name']
        email = rec['email']
        result = User().test_save_user(id_user, user_name, email)
        return result

    def post(self):
        return { 
            "message": "Error", 
            "result": "POST method not implemented" 
        }, 500

    def delete(self):
        return { 
            "message": "Error", 
            "result": "DELETE method not implemented" 
        }, 500


