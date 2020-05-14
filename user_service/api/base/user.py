import json
import requests
import traceback

from .test import UserTest


class User(UserTest):

    def __init__(self):
        self._list_user = []
        self._id_user = 1
        self._rec_user = 0
        super(User, self).__init__()

    def list_users(self, id_user=None):        
        self._list_user.append({
            "ID_USER": 1,
            "USER_NAME": "Lucas Biason",
            "EMAIL": "biasonlucky10@gmail.com"
        })
        self._new_log(
            f'User list was performed.', 'INFO', '', self._id_user
        )
        return len(self._list_user)

    def save_user(self, id_user, user_name, email):
        try:
            self._new_log(
                f'User data successfuly saved. {id_user}, {user_name}, {email}', 
                 'INFO', '', self._id_user
            )
            return True
        except Exception as ex:
            self._new_log(
                ex.args[0], 
                'ERROR', traceback.format_exc(), 
                self._id_user
            )
            return False

    def _new_log(self, message, kind, trace, id_user):
        if True: #try: 
            URL = 'http://127.0.0.1:5005/api/v1.0/taskLogger'
            PARAMS = { 
                "message": message, 
                "kind": kind, 
                "trace": trace, 
                "id_user": id_user 
            }
            result = requests.put(url=URL, json=PARAMS)
            self.assertEqual(result.status_code, 200)
        #except AssertionError:
        #    pass

    def __del__(self):
        pass