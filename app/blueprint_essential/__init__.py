from flask import Blueprint

blueprint_essential = Blueprint('blueprint_essential', __name__, url_prefix='/blueprint_essential')

from . import views
