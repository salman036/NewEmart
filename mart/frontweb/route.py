from datetime import timedelta
import datetime
from celery import Celery
from flask import *
from mart import db, app, mail
from flask_mail import Message
from mart.constant.appConstant import Constant
from mart.frontweb.forms import UserPost
from mart.models import Categories, Subcategories, Products
from mart.models import PostUser
from celery.schedules import crontab
from celery_once import QueueOnce

celery = Celery('hello', broker="redis://guest@localhost//", backend='redis')

front_web = Blueprint('front_web', __name__)


@front_web.route('/', methods=[Constant.GET, Constant.POST])
def front_home():
    all_cat = Categories.query.all()

    return render_template('frontHome.html', all_cat=all_cat)


@front_web.route('/sub/<string:sub_id>', methods=[Constant.GET, Constant.POST])
def show_sub_cat(sub_id):
    sub_cat = Subcategories.query.filter_by(categories_id=sub_id)
    return render_template('front_sub_cat.html', sub_cat=sub_cat)


@front_web.route('/product/<string:pro_id>', methods=[Constant.GET, Constant.POST])
def show_pro_id(pro_id):
    pro_item = Products.query.filter_by(sub_cat_id=pro_id)
    return render_template('front_products.html', pro_item=pro_item)


@front_web.route('/post_front', methods=[Constant.GET, Constant.POST])
def front_post():
    form = UserPost()
    user_post = PostUser.query.all()
    if form.validate_on_submit():
        post_user = PostUser(title=form.title.data, content=form.content.data)
        db.session.add(post_user)
        db.session.commit()
        msg = Message('Hello', sender='salmansaleem036@gmail.com', recipients=['idreesrehan234@gmail.com'])
        msg.body = "This is the email body"
        mail.send(msg)

        return redirect(url_for('front_web.front_home'))
    return render_template('add_front_post.html', form=form, user_post=user_post)


@front_web.route('/show_user_post', methods=[Constant.GET, Constant.POST])
def show_user_post():
    user_post = PostUser.query.all()
    return render_template('show_user_post.html', user_post=user_post)


@front_web.route('/post_front/<int:id>', methods=[Constant.GET, Constant.POST])
def active_post_user(id):
    post_user = PostUser.query.get_or_404(id)

    if post_user.status == False:
        post_user.status = True
        db.session.commit()
    else:
        post_user.status = False
        db.session.commit()
    return redirect(url_for('front_web.front_post'))


# here celery tasks
@celery.task
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    with app.app_context():
        mail.send(msg)


@celery.task
def index():
    try:
        post = PostUser.query.filter_by(status=False).first()
        print(post.post_at < datetime.datetime.now() - timedelta(minutes=3))
        if post.post_at < datetime.datetime.now() - timedelta(minutes=3):
            print('Come here')
            db.session.delete(post)
            db.session.commit()
    except:
        print('empty table')
    return 'sent'


@celery.task()
def send_email_notification():
    try:
        post = PostUser.query.filter_by(status=False).first()
        print(post.post_at < datetime.datetime.now() - timedelta(minutes=1))
        if post.post_at < datetime.datetime.now() - timedelta(minutes=1):
            print('email send')
            msg = Message('Hello', sender='salmansaleem036@gmail.com', recipients=['idreesrehan234@gmail.com'])
            msg.body = "After two minutes post will expire"
            send_async_email(msg)
    except:
        print('No email')
    return 'Email send'


@celery.task(bind=True)
def check():
    print('check')
    return ''


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        timedelta(seconds=30),
        index,

    )
    sender.add_periodic_task(
        timedelta(seconds=30),
        send_email_notification,

    )
    # sender.add_periodic_task(
    #     timedelta(seconds=30),
    #
    #     check,
    # )
