import datetime
import json
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import login_user
from flask_login import logout_user

from . import blueprint_auth
from .forms import RegisterForm
from .forms import LoginForm
from .utils_cms import generate_code
from .utils_cms import send_sms_code
from ..models import db
from ..models import User


@blueprint_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        login_user(user)
        return redirect(url_for('blueprint_home.index'))

    return render_template('auth/login.html', form=form)


@blueprint_auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()


@blueprint_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User.query.filter_by(phone=form.phone.data).first()
        new_user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for('blueprint_auth.login'))

    return render_template('auth/register.html', form=form)


@blueprint_auth.route('/sms_code/<string:phone>', methods=['GET', 'POST'])
def sms_code(phone):
    user = User.query.filter_by(phone=phone).first()
    if not user:
        ret = {'result': 'error'}
        return json.dumps(ret)

    code = generate_code()
    ret = send_sms_code(phone, code)
    if not ret:
        ret = {'result': 'error'}
        return json.dumps(ret)

    user.sms_code = code
    user.updated_at = datetime.datetime.now()
    db.session.commit()
    ret = {'result': 'success'}
    return json.dumps(ret)

