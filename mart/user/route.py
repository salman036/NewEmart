from flask import *
from mart.constant.appConstant import Constant
from mart.user.forms import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm
from mart.models import Users
from mart import bcrypt, db
from flask_login import logout_user, login_user, current_user
from mart.user.utils import send_reset_email
from werkzeug.security import generate_password_hash, check_password_hash

user = Blueprint('user', __name__)


@user.route('/register', methods=[Constant.POST, Constant.GET])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        hashed_password = generate_password_hash(form.password.data)
        try:
            user = Users(name=form.name.data, username=form.username.data, email=form.email.data,
                         password=hashed_password)
            db.session.add(user)
            db.session.commit()
        except:
            return jsonify({
                "status": "error",
                "message": "Could not add user"
            })
        # return jsonify({
        #     "status": "success",
        #     "message": "User added successfully"
        # }), 201
        flash(f'{Constant.REGISTER_SUCCESSFULLY}', f'{Constant.INFO_FLASH_MESSAGE}')
        return redirect(url_for('user.login'))
    return render_template('register.html', title='Register', form=form)


@user.route('/login', methods=[Constant.GET, Constant.POST])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'{Constant.LOGIN_SUCCESSFULLY}', 'success')
            # return jsonify({
            #     "status":"success",
            #     "message":"login success"
            # })
            return redirect(url_for('main.home'))
        else:
            flash(Constant.INVALID_EMAIL_OR_PASSWORD, f'{Constant.DANGER}')
    return render_template('login.html', form=form)


@user.route('/reset_password', methods=[Constant.POST, Constant.GET])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        return redirect(url_for('user.login'))
    return render_template('request_reset.html', title='Reset Request', form=form)


@user.route('/reset_password/<token>', methods=[Constant.POST, Constant.GET])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = Users.verify_reset_token(token)
    if user is None:
        flash(Constant.INVALID_TOKEN, 'warning')
        return redirect(url_for('user.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hased_password = generate_password_hash(form.password.data)
        user.password = hased_password
        db.session.commit()
        flash(Constant.PASSWORD_UPDATE, 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_password.html', title='Reset Password', form=form)


@user.route('/logout', methods=[Constant.POST, Constant.GET])
def logout():
    logout_user()
    return redirect(url_for('user.login'))
