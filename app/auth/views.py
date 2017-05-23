from flask import current_app
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import login_user

from . import auth_blueprint
from .forms import RegisterForm
from .forms import LoginForm
from ..models import db
from ..models import User


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        login_user(user)
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User()
        new_user.phone = form.phone.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/sms_code', methods=['GET', 'POST'])
def sms_code():
    return current_app['']