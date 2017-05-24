from flask import Flask

from .config import configs
from .models import db

from .vendors import bcrypt
from .vendors import login_manager

from .blueprint_auth import blueprint_auth
from .blueprint_home import blueprint_home


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # register blueprints here.
    app.register_blueprint(blueprint_auth)
    app.register_blueprint(blueprint_home)

    return app
