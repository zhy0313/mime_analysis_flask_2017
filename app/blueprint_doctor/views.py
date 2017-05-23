from flask_login import login_required
from . import blueprint_doctor


@blueprint_doctor.route('/disease_count/')
@login_required
def disease_count():
    pass

