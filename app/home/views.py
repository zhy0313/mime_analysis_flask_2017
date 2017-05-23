from flask import render_template
from flask_login import login_required
from . import home_blueprint


@home_blueprint.route('/')
@home_blueprint.route('/index/')
@login_required
def index():
    return render_template('home.html')

