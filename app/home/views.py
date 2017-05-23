from flask import render_template
from . import home_blueprint


@home_blueprint.route('/')
@home_blueprint.route('/index/')
def index():
    return render_template('home.html')

