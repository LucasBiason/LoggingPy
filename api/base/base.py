import json

from flask import jsonify
from decimal import Decimal


class Base:

    @staticmethod
    def to_json_route(self, message, status=int):
        return jsonify({ "message": message }), status

    @staticmethod
    def threat_colunms(row):
        is_str = type(row) is str

        if not is_str:
            retorno = list(row)

            for i, item in enumerate(retorno):
                if type(retorno[i]) == str:
                    retorno[i] = retorno[i].replace('"', '') 
                elif type(retorno[i]) == int:
                    pass
                elif type(retorno[i]) == Decimal:
                    retorno[i] = float(item)
        elif is_str:
            retorno = row.replace('"', '') 

        return retorno
    
    @staticmethod
    def to_json(lista):
        lista1 = []
        lista1.extend(list(map(Base.threat_colunms, lista)))
        return json.dumps(lista1)