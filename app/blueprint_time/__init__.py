from flask import Blueprint

blueprint_time = Blueprint('blueprint_time', __name__, template_folder='../templates')

from . import views
