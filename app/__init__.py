from flask import Flask

from .config import configs
from .models import db

from .vendors import bcrypt
from .vendors import login_manager

from .blueprint_auth import blueprint_auth
from .blueprint_time import blueprint_time
from .blueprint_region import blueprint_region
from .blueprint_doctor import blueprint_doctor


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # register blueprints here.
    app.register_blueprint(blueprint_auth)
    app.register_blueprint(blueprint_time)
    app.register_blueprint(blueprint_region)
    app.register_blueprint(blueprint_doctor)

    return app
