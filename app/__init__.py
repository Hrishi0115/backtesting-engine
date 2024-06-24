# This file initialises the Flask application and can be used to set up the app configuration

# including initialization logic in the `__init__.py` file is a common practice in Flask applications to set up the application instance.

from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_routes(app)
    return app

