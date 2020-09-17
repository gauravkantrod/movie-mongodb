from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from os import environ
from resources.errors import errors


app = Flask(__name__)
app.config.from_object('config.ProdConfig')

api = Api(app, errors=errors)

initialize_db(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
initialize_routes(api)


if __name__ == "__main__":
    app.run()
