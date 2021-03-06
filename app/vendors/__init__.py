from flask_bcrypt import Bcrypt
from flask_login import LoginManager


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'blueprint_auth.login'
