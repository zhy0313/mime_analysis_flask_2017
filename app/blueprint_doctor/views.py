from flask_login import login_required
from . import blueprint_doctor


@blueprint_doctor.route('/index/')
@login_required
def index():
    pass

