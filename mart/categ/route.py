from flask import *
from mart.constant.appConstant import Constant
from mart.models import Categories, Subcategories, Products
from mart import db
from mart.categ.forms import CategoryForm, SubCategoryForm, ProductForm, SaleForm
from flask_login import login_required
from mart.categ.utils import save_picture

categ = Blueprint('categ', __name__)


@categ.route('/add_cat', methods=[Constant.GET, Constant.POST])
@login_required
def add_cat():
    form = CategoryForm()
    categories = Categories.query.all()

    if form.validate_on_submit():
        try:
            if form.image_file.data:
                save_image = save_picture(form.image_file.data)
            cat = Categories(name=form.name.data, image_file=save_image)
            db.session.add(cat)
            db.session.commit()
            return redirect(url_for('categ.add_cat'))
        except:
            flash(f'{Constant.IMAGE_FILED_EMPTY}', f'{Constant.DANGER}')
    return render_template('add_category.html', form=form, categories=categories, legend='Add Category',
                           title='Add Category')


@categ.route('/add_sub_cat', methods=[Constant.GET, Constant.POST])
@login_required
def add_sub_cat():
    if request.method == Constant.POST:
        cat = request.form.get('select_value')
    else:
        cat = None
    form = SubCategoryForm()
    categories = Categories.query.all()
    sub_catagories = Subcategories.query.all()

    for one_cat in categories:
        if cat == one_cat.name:
            cat_id = one_cat.name
            print(cat_id)
            break
    if form.validate_on_submit():
        try:
            if form.image_file.data:
                save_image = save_picture(form.image_file.data)
            cat = Subcategories(name=form.name.data, image_file=save_image, categories_id=cat_id)
            db.session.add(cat)
            db.session.commit()
            return redirect(url_for('categ.add_sub_cat'))
        except:
            flash(f'{Constant.IMAGE_FILED_EMPTY}', f'{Constant.DANGER}')
    return render_template('add_sub_cat.html', form=form, categories=categories, sub_catagories=sub_catagories,
                           title='Add new quote', legend='Add Sub Category')


@categ.route('/add_product', methods=[Constant.GET, Constant.POST])
@login_required
def add_product():
    if request.method == Constant.POST:
        cat = request.form.get('select_value')
    else:
        cat = None
    form = ProductForm()
    sub_categories = Subcategories.query.all()
    products = Products.query.all()
    for one_cat in sub_categories:
        if cat == one_cat.name:
            cat_id = one_cat.name
            print(cat_id)
            break
    if form.validate_on_submit():
        if form.image_file.data:
            save_image = save_picture(form.image_file.data)
        product = Products(name=form.name.data, total_quantity=form.total_quantity.data, unit=form.unit.data,
                           net_price=form.net_price.data, sale_price=form.sale_price.data,
                           image_field=save_image, description=form.description.data, sub_cat_id=cat_id)
        db.session.add(product)
        db.session.commit()
        flash(f'{Constant.SAVE_SUCCESSFULLY}', f'{Constant.FLASH_MESSAGE_SUCCESS}')
        return redirect(url_for('categ.add_product'))

    return render_template('add_products.html', form=form, sub_categories=sub_categories, products=products)


@categ.route('/add_cat/<int:id>', methods=[Constant.GET, Constant.POST])
@login_required
def active_action(id):
    sub_id = Categories.query.get_or_404(id)

    if sub_id.deleted == False:
        sub_id.deleted = True
        db.session.commit()
    else:
        sub_id.deleted = False
        db.session.commit()
    return redirect(url_for('categ.add_cat'))


@categ.route('/add_sub_cat/<int:id>', methods=[Constant.GET, Constant.POST])
@login_required
def active_sub_cat(id):
    sub_id = Subcategories.query.get_or_404(id)

    if sub_id.deleted == False:
        sub_id.deleted = True
        db.session.commit()
    else:
        sub_id.deleted = False
        db.session.commit()
    return redirect(url_for('categ.add_sub_cat'))


@categ.route('/add_sub_cat/delete/<int:id>', methods=[Constant.GET, Constant.POST])
@login_required
def delete_sub_cat(id):
    sub_id = Subcategories.query.get_or_404(id)
    db.session.delete(sub_id)
    db.session.commit()
    flash(f'{Constant.DELETE_SUCCESSFULLY}', f'{Constant.FLASH_MESSAGE_SUCCESS}')
    return redirect(url_for('categ.add_sub_cat'))


@categ.route('/update/<int:sub_catID>', methods=[Constant.POST, Constant.GET])
@login_required
def update_sub_cat(sub_catID):
    if request.method == Constant.POST:
        cat = request.form.get('select_value')
    else:
        cat = None
    form = SubCategoryForm()
    categories = Categories.query.all()
    sub_catagories = Subcategories.query.all()
    for one_cat in categories:
        if cat == one_cat.name:
            cat_id = one_cat.name
            # print(cat_id)
            break

    sub_cat = Subcategories.query.get_or_404(sub_catID)
    if form.validate_on_submit():
        if form.image_file.data:
            image_save = save_picture(form.image_file.data)
        sub_cat.categories_id = cat_id
        sub_cat.name = form.name.data
        sub_cat.image_file = image_save
        db.session.commit()
        flash(f'{Constant.UPDATE_SUCCESSFULLY}', f'{Constant.FLASH_MESSAGE_SUCCESS}')
        return redirect(url_for('categ.add_sub_cat'))
    elif request.method == Constant.GET:
        form.image_file.data = sub_cat.image_file
        form.name.data = sub_cat.name
    return render_template('add_sub_cat.html', form=form, categories=categories, sub_catagories=sub_catagories,
                           title='Update Sub Cat', legend='Update Sub Category')


@categ.route('/add_cat/update/<int:my_cat_id>', methods=[Constant.POST, Constant.GET])
@login_required
def update_cat(my_cat_id):
    categories = Categories.query.all()
    form = CategoryForm()
    my_cat_id = Categories.query.get_or_404(my_cat_id)
    if form.validate_on_submit():
        if form.image_file.data:
            save_image = save_picture(form.image_file.data)
        my_cat_id.name = form.name.data
        my_cat_id.image_file = save_image
        db.session.commit()
        flash(f'{Constant.UPDATE_SUCCESSFULLY}', f'{Constant.FLASH_MESSAGE_SUCCESS}')
        return redirect(url_for('categ.add_cat'))
    elif request.method == Constant.GET:
        form.name.data = my_cat_id.name
    return render_template('add_category.html', form=form, categories=categories,
                           title='Update Cat', legend='Update Category Name')


@categ.route('/add_cat/delete/<int:my_cat_id>', methods=[Constant.POST, Constant.GET])
@login_required
def delete_cat(my_cat_id):
    cat_delete_id = Categories.query.get_or_404(my_cat_id)
    db.session.delete(cat_delete_id)
    db.session.commit()
    return redirect(url_for('categ.add_cat'))


@categ.route('/sale', methods=[Constant.GET, Constant.POST])
def sale():
    if request.method == Constant.POST:
        cat = request.form.get('select_value')
    else:
        cat = None

    print(cat)
    produts = Products.query.all()
    form = SaleForm()
    if form.validate_on_submit():
        try:
            c = form.unit.data * form.quantity.data
            form.total.data = c
            print(c)
        except:
            pass
    return render_template('sale.html', produts=produts, form=form)
