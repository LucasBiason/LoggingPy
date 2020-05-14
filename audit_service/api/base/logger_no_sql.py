
from datetime import datetime
from pymongo import MongoClient

from .tests import LoggerNoSQLTest


class LoggerNoSQL(LoggerNoSQLTest):

    def __init__(self):
        """
        Class that write and read logging on any kind info or error of the application
        """
        connection_string = "mongodb+srv://{}:{}@{}/test?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string.format(
            'lucasbiason', 'mongo2525', 'cluster0-9hvcq.gcp.mongodb.net'
        ))
        self.ids_inserted = []

        self._test_connection()

        self._list_of_logs = []
        
    def add_log(self, message, kind, trace, idUser):
        """
        Creates a new log info or error and insert on database
        """

        tb_logInfo = self.db.tb_logInfo

        result = tb_logInfo.insert_one({
            'ID_USER': idUser,
            'DATE_OF': datetime.now().strftime('%m/%d/%Y %H:%M'),
            'MESSAGE': message,
            'LEVEL': kind,
            'TRACE': trace
        })
        return result._WriteResult__acknowledged

    def list_logs(self, _date, start, limit):
        """
        Creates a filtered list of collextion logs
        Return: returns a length of records found
        """
        tb_logInfo = self.db.tb_logInfo
        recipes = tb_logInfo.find({
            'DATE_OF': { '$gt': _date }
        }).sort('DATE_OF', -1).skip(start).limit(limit)

        for item in recipes:
            self._list_of_logs.append((
                item['DATE_OF'], 
                item['LEVEL'], 
                item['MESSAGE'], 
                item['TRACE'])
            )
        return len(self._list_of_logs)
