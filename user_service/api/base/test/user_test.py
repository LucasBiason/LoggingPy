import unittest


class UserTest(unittest.TestCase):
    
    def test_list_users(self, id_user=None):
        try:
            self.assertGreater(
                self.list_users(id_user=id_user), 
                0
            )
            return { 
                    "message": "Ok", 
                    "result": self._list_user 
            }, 200
        except AssertionError as ae:
            _message = ae.args[0]
            return { 
                    "message": "Error", 
                    "result": _message 
            }, 500

    def test_save_user(self, id_user, user_name, email):
        try:
            self.assertTrue(self.save_user(id_user, user_name, email))
            return { "message": "Ok", 
                "result": f'User data successfuly saved. {id_user}, {user_name}, {email}' 
            }, 200
        except AssertionError as ae:
            _message = ae.args[0]
            return { 
                    "message": "Error", 
                    "result": ae.args[0] 
            }, 500
