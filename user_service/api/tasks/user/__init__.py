from flask_restful import Api
from main_user import flaskApp
from api.tasks.user.task_user import TaskUser

restServer = Api(flaskApp)

restServer.add_resource(TaskUser, "/api/v1.0/taskUser")