from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from mart.config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emart.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'user.login'
login.login_message_category = 'info'

from mart.models import Users

# BluePrints route here
from mart.user.route import user
from mart.main.route import main
from mart.categ.route import categ
from mart.dashboard.route import dashb
from mart.api.route import api
from mart.custome_pages.route import errors
from mart.frontweb.route import front_web

app.register_blueprint(user)
app.register_blueprint(main)
app.register_blueprint(categ)
app.register_blueprint(dashb)
app.register_blueprint(api)
app.register_blueprint(errors)
app.register_blueprint(front_web)
