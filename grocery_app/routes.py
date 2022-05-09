from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    # Create a GroceryStoreForm
    grocery_form = GroceryStoreForm()
    # If form was submitted and was valid:
    # - create a new GroceryStore object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the store detail page.
    if request.method == 'POST':
        # create obj & save to db
        grocery_store = GroceryStore(title=request.form.get('title'), address=request.form.get('address'))
        db.session.add(grocery_store)
        db.session.commit()
        flash('Added grocery form')
        return redirect(url_for('main.store_detail'))
        
    # Send the form to the template and use it to render the form fields
    return render_template('new_store.html', form=grocery_form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    # Create a GroceryItemForm
    grocery_item = GroceryItemForm()

    # If form was submitted and was valid:
    # - create a new GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.
    if request.method == 'POST':
        grocery_item = GroceryItem(
            name=request.form.get('name'), 
            price=request.form.get('price'),
            category=request.form.get('category'),
            photo_url=request.form.get('photo_url'),
            store=request.form.get('store')
        )
        db.session.add(grocery_item)
        db.session.commit()

        flash('Added grocery item')
        
        return redirect(url_for('main.item_detail'))
    else:
        # TODO: Send the form to the template and use it to render the form fields
        return render_template('new_item.html', form=grocery_item)


@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    # Create a GroceryStoreForm and pass in `obj=store`

    # If form was submitted and was valid:
    # - update the GroceryStore object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the store detail page.

    # Send the form to the template and use it to render the form fields
    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # Create a GroceryItemForm and pass in `obj=item`

    # If form was submitted and was valid:
    # - update the GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.

    # Send the form to the template and use it to render the form fields
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item)

