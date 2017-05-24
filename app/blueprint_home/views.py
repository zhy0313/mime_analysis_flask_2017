from flask import render_template
from flask_login import login_required
from . import blueprint_home


@blueprint_home.route('/')
@blueprint_home.route('/index/')
@login_required
def index():
    return render_template('home.html')

@blueprint_home.route('/daily_count/')
@login_required
def daily_count():
    pass


@blueprint_home.route('/region_count/')
@login_required
def region_count():
    pass
