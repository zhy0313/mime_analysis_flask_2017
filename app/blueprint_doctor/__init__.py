from flask import Blueprint

blueprint_doctor = Blueprint('blueprint_doctor',
                             __name__,
                             url_prefix='/doctor',
                             template_folder='../templates/doctor')
