from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from mart.models import Users
from mart.constant.appConstant import Constant
import re


class RegisterForm(FlaskForm):
    name = StringField(f'{Constant.NAME}', validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(f'{Constant.USER_NAME}',
                           validators=[DataRequired(), Length(min=2, max=15),
                                       ])
    email = StringField(f'{Constant.EMAIL}', validators=[DataRequired(), Length(min=2, max=50), Email(),
                                                         Regexp(f"{Constant.REGULAR_EXPRESSION_EMAIL}",
                                                                message=Constant.REGULAR_EXPRESSION_EMAIL_MESSAGE)])
    password = PasswordField(f'{Constant.PASSWORD}',
                             validators=[Regexp(f"{Constant.REGULAR_EXPRESSION}",
                                                message=f"{Constant.REGULAR_EXPRESSION_MESSAGE}"),
                                         DataRequired(), Length(max=20)
                                         ])
    confirm_password = PasswordField(f'{Constant.CONFIRM_PASSWORD}', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(f'{Constant.SUBMIT}')

    def validate_username(self, username):
        users = Users.query.filter_by(username=username.data).first()
        if users:
            raise ValueError(f'{Constant.USER_NAME_ALREADY_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')

    def validate_email(self, email):
        users = Users.query.filter_by(email=email.data).first()
        if users:
            raise ValueError(f'{Constant.EMAIL_ALREADY_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')

    # def validate(self):
    #     if re.match('[0-9]', self.password) is None:
    #         raise ValueError("Make sure your password has a number in it")
    #     elif re.search('[A-Z]', self.password) is None:
    #         raise ValueError("Make sure your password has a capital letter in it")


class LoginForm(FlaskForm):
    email = StringField(Constant.EMAIL, validators=[DataRequired(), Length(min=2, max=25), Email()])
    password = PasswordField(Constant.PASSWORD, validators=[DataRequired(), Length(min=2, max=25)])
    submit = SubmitField(f'{Constant.SUBMIT}')


class RequestResetForm(FlaskForm):
    email = StringField(Constant.EMAIL, validators=[DataRequired(), Length(min=2, max=25), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValueError(f'{Constant.EMAIL_DOES_NOT_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(Constant.PASSWORD, validators=[DataRequired()])
    confirm_password = PasswordField(Constant.CONFIRM_PASSWORD,
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(Constant.RESET_PASSWORD)
