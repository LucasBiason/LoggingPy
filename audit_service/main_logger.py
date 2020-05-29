from flask import Flask

flaskApp = Flask(__name__)

if __name__ == '__main__':
    from api.tasks import *
    flaskApp.run(host='0.0.0.0', port=5005, use_reloader=True)