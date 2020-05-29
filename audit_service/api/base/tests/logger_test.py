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
        Try to connect on MongoDB instance and try to create collections
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
