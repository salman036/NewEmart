from flask import *
from mart.constant.appConstant import Constant

api = Blueprint('api', __name__)


@api.route('/users', methods=[Constant.GET])
def get_user():
    pass
