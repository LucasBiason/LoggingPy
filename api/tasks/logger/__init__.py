from flask_restful import Api
from main_logger import flaskApp
from api.tasks.logger.task_logger import TaskLogger

restServer = Api(flaskApp)

restServer.add_resource(TaskLogger, "/api/v1.0/taskLogger")