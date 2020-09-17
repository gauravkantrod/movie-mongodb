from flask import Flask
import logging
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from os import environ
from resources.errors import errors


app = Flask(__name__)

#once set cannot be changed.
logging.basicConfig(filename='log.log', level=logging.DEBUG,\
                    format=" %(asctime)s :: %(levelname)s :: %(name)s :: %(threadName)s :: %(message)s")

app.config.from_object('config.DevConfig')

api = Api(app, errors=errors)

initialize_db(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
initialize_routes(api)


if __name__ == "__main__":
    app.run()
