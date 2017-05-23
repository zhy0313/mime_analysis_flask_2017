from flask import Blueprint

blueprint_home = Blueprint('blueprint_home', __name__, template_folder='../templates')

from . import views
