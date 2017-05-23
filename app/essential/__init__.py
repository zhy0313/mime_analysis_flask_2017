from flask import Blueprint

essential_blueprint = Blueprint('essential', __name__, url_prefix='/essential')

from . import views
