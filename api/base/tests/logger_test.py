import unittest
import traceback

from .data import TEST_DATA


class LoggerNoSQLTest(unittest.TestCase):
    
    def _test_connection(self):
        """
        Tests the checkserver method to connect on database
        """
        try:
            self.assertTrue(self.check_server(), True)
        except AssertionError as ae:
            raise Exception('Failure to connect in database. \n',
                ae.args[0])
            
    def check_server(self):
        """
        Try to connect on MongoDB cloud instance and try to create collections
        Return: True if the database is reachable and False on any problem encontered on that
        """
        try:
            self.client.server_info()
            self.db = self.client.logRecipe
            self.__start_tables()
            return True
        except:
            return False

    def __start_tables(self):
        """
        Starts to create table collections if they don't created yet
        """
        for item in TEST_DATA:
            self.__create_table(item['tableName'], item['firstRec'])

    def __create_table(self, table_name, first_rec):
        """
        Checks if tableName is created and do the table with fields
        described in firstRec variable if don't.
        Return: 
            returns True if table was successfully created
        """
        if table_name not in self.db.collection_names():
            tbl = self.db[table_name]
            tbl.insert_one(first_rec)
            tbl.delete_one(first_rec)
            return True
        return False

    def test_add_log(self, message, kind, trace, id_user):
        """
        Tests the addLog method
        Return: returns number of inserted record(s). One record will inserted by default
        """

        try:
            self.assertTrue(
                self.add_log(message, kind, trace, id_user)
            )
            return { 
                    "message": "Ok", 
                    "result": "1 record of Logging was inserted on the database" 
            }, 200
        except AssertionError as ae:
            return { 
                    "message": "Error", 
                    "result": ae.args[0] 
            }, 500

    def test_list_logs(self, data, start, limit):
        """
        Tests the list of logs
        Return: returns the list_of_logs filled list 
        """

        try:
            self.assertGreater(
                self.list_logs(data, start, limit), 0
            )
            return {
                 "message": "Ok", 
                 "result": self._list_of_logs 
                 }, 200
        except AssertionError as ae:
            return { 
                "message": "Error", 
                "result": ae.args[0] 
            }, 500
