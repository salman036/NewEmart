from mart import *
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from mart.utils import QueryWithSoftDelete


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expire_time=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_time)
        token = s.dumps({'user_id': self.id}).decode('utf-8')
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)

    def __repr__(self):
        return f"User('{self.name}', '{self.username}', '{self.email}', '{self.password}')"


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    image_file = db.Column(db.String(125), default='default.jpg')
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
    deleted = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f"(Category('{self.name}', '{self.image_file}', '{self.create_at}'))"


class Subcategories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    image_file = db.Column(db.String(125), default='default.jpg')
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
    deleted = db.Column(db.Boolean(), default=True)
    categories_id = db.Column(db.String(100), db.ForeignKey('categories.name'))

    def __repr__(self):
        return f"(SubCategories('{self.name}', '{self.image_file}', '{self.create_at}', '{self.categories_id}', '{self.deleted}'))"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    total_quantity = db.Column(db.Integer)
    unit = db.Column(db.Integer)
    image_field = db.Column(db.String(60), default='default.jpg')
    description = db.Column(db.String(120), nullable=False)
    net_price = db.Column(db.Float)
    sale_price = db.Column(db.Float, default=0)
    sub_cat_id = db.Column(db.String(60), db.ForeignKey('subcategories.name'))

    def __repr__(self):
        return f"Products('{self.name}', '{self.total_quantity}', '{self.unit}', '{self.image_field}', '{self.net_price}', " \
            f"'{self.sale_price}')"


class PostUser(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(60))
    status = db.Column(db.Boolean(), default=False)
    post_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f"PostUser('{self.title}', '{self.content}', '{self.status}', '{self.post_at}')"
