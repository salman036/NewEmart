from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, FloatField, TextAreaField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from mart.models import Categories, Subcategories
from mart.constant.appConstant import Constant, Product
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField(f'{Constant.NAME}', validators=[DataRequired()])
    image_file = FileField(f'{Constant.UPLOAD_IMAGE}', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField(f'{Constant.SUBMIT}')

    def validate_name(self, name):
        cat = Categories.query.filter_by(name=name.data).first()
        if cat:
            raise ValidationError(f'{Constant.NAME_ALREADY_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')


class SubCategoryForm(FlaskForm):
    name = StringField(f'{Constant.NAME}', validators=[DataRequired()])
    image_file = FileField(f'{Constant.UPLOAD_IMAGE}', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField(f'{Constant.SUBMIT}')

    def validate_name(self, name):
        sub_cat = Subcategories.query.filter_by(name=name.data).first()
        if sub_cat:
            raise ValueError(f'{Constant.NAME_ALREADY_EXIST}', f'{Constant.DANGER}')


class ProductForm(FlaskForm):
    name = StringField(f'{Product.NAME}', validators=[DataRequired(), Length(min=2, max=50)])
    total_quantity = IntegerField(f'{Product.TOTAL_QUANTITY}', validators=[DataRequired()])
    unit = IntegerField(f'{Product.UNIT}', validators=[DataRequired()])
    image_file = FileField(f'{Product.IMAGE}', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    description = TextAreaField(f'{Product.DESCRIPTION}', validators=[DataRequired()])
    net_price = FloatField(f'{Product.NET_PRICE}', validators=[DataRequired()])
    sale_price = FloatField(f'{Product.SALE_PRICE}', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SaleForm(FlaskForm):
    unit = IntegerField(f'{Product.UNIT}', validators=[DataRequired()])
    quantity = IntegerField(f'{Product.TOTAL_QUANTITY}', validators=[DataRequired()])
    total = StringField(f'{Product.TOTAL}')
    submit = SubmitField('Submit')
