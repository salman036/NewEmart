from flask_mail import Message
from mart import mail
from flask import render_template, flash
from mart.constant.appConstant import Constant
import re


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset message', sender='noreply@gmail.com', recipients=[user.email])
    msg.html = render_template('include/SentEmail.html', token=token, _external=True)
    flash(f'{Constant.RESET_PASSWORD_EMAIL_SEND}', f'{Constant.INFO_FLASH_MESSAGE}')
    mail.send(msg)

    return "Send"


def validate():
    while True:
        password = raw_input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break
