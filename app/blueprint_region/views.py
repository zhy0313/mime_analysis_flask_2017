from flask_login import login_required
from . import blueprint_region


@blueprint_region.route('/index/')
@login_required
def index():
    pass

