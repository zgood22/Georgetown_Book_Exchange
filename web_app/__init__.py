# this is the "web_app/__init__.py" file...
from flask import Flask, Blueprint

from web_app.routes import register_routes


register_routes = Blueprint("register", __name__) #enures register_routes is correctly defined and imported 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(register_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
