from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import EqualTo

from ..models import User


class LoginForm(FlaskForm):
    phone = StringField('Phone', [DataRequired(), Length(max=11)])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False
        # if the user exist
        user = User.query.filter_by(phone=self.phone.data).first()
        if not user:
            return False
        # if the passwords not match
        if not user.check_password(self.password.data):
            return False

        return True


class RegisterForm(FlaskForm):
    phone = StringField('Phone', [DataRequired(), Length(max=11)])
    code = StringField('Code', [DataRequired(), Length(max=4)])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate(self):
        check_validate = super(RegisterForm, self).validate()
        if not check_validate:
            return False
        # Is the username already being used
        user = User.query.filter_by(phone=self.phone.data).first()
        if user:
            return False

        return True

