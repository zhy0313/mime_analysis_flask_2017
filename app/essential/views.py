from flask_login import login_required
from . import essential_blueprint


@essential_blueprint.route('/daily_count/')
@login_required
def daily_count():
    pass


@essential_blueprint.route('/region_count/')
@login_required
def region_count():
    pass
