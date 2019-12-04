from flask import *
from mart.constant.appConstant import Constant

dashb = Blueprint('dashb', __name__)


@dashb.route('/dashboard', methods=[Constant.GET, Constant.POST])
def dashboard():
    return render_template('dashboard.html')
