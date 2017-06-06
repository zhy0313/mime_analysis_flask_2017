from flask import Blueprint

blueprint_region = Blueprint('blueprint_region',
                             __name__,
                             url_prefix='/region',
                             template_folder='../templates')

from . import views
