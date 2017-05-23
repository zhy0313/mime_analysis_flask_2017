from flask_login import login_required
from . import blueprint_essential


@blueprint_essential.route('/daily_count/')
@login_required
def daily_count():
    pass


@blueprint_essential.route('/region_count/')
@login_required
def region_count():
    pass
