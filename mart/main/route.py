from flask import *
from mart.constant.appConstant import Constant
from flask_login import login_required
from mart.models import Subcategories, Categories, Products, PostUser
from mart.main.forms import UserPost
from mart import db

main = Blueprint('main', __name__)


@main.route('/home', methods=[Constant.GET, Constant.POST])
def home():
    sub_cat = Subcategories.query.all()
    cat = Categories.query.all()
    products = Products.query.all()
    return render_template('home.html', cat=cat, sub_cat=sub_cat, products=products)



