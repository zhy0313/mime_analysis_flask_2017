import datetime
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import login_user
from flask_login import logout_user

from . import auth_blueprint
from .forms import RegisterForm
from .forms import LoginForm
from .utils_cms import generate_code
from .utils_cms import send_sms_code
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


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()


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


@auth_blueprint.route('/sms_code/<string:phone>', methods=['GET', 'POST'])
def sms_code(phone):
    user = User.query.filter_by(phone=phone).first()
    if not user:
        return 'error'

    code = generate_code()
    ret = send_sms_code(phone, code)
    if not ret:
        return 'error'

    user.sms_code = code
    user.updated_at = datetime.datetime.now()
    db.session.commit()
    return 'success'
