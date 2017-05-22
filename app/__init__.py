from flask import Flask

from .config import configs
from .models import db

from .vendors import bcrypt
from .vendors import login_manager

from .auth import auth_blueprint
from .home import home_blueprint


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # register blueprints here.
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)

    return app
