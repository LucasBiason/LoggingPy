import json

from flask_restful import Resource
from flask import request

from api.base.logger_no_sql import LoggerNoSQL

class TaskLogger(Resource):

    def __init__(self):
       pass

    def get(self):
        rec = request.get_json(force=True)
        log = LoggerNoSQL()
        try:
            result = log.list_logs(
                rec['date'], 
                rec['start'], 
                rec['limit']
            )
            return {
                 "message": "Ok", 
                 "result": result
            }, 200
        except Exception as e:
            return { 
                "message": "Error", 
                "result": e.args[0] 
            }, 500
        
        return result

    def put(self):
        rec = request.get_json(force=True)
        log = LoggerNoSQL()
        try:
            result = log.add_log(
                rec['message'], 
                rec['kind'], 
                rec['trace'], 
                rec['id_user']
            )
            if not result:
                raise Exception()
            
            return { 
                    "message": "Ok", 
                    "result": "1 record of Logging was inserted on the database" 
            }, 200
        except Exception as e:
            return { 
                    "message": "Error", 
                    "result": e.args[0] 
            }, 500

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
