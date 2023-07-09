from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc
from database_setup import Base, Restaurant, MenuItem

# DB connection
engine = create_engine('sqlite:///restaurantmenu.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()


app = Flask(__name__)
# home page
@app.route('/')
@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html',restaurants=restaurants)


# add a new restaurant
@app.route('/restaurants/new/', methods = ['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        new_restaurant = Restaurant(name=request.form['new_restaurant'])
        session.add(new_restaurant)
        session.commit()
        flash('New Restaurant Created!')
        return redirect(url_for('restaurants'))
    else:
        return render_template('newRestaurant.html')


# edit a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/',methods=['GET','POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        restaurant.name = request.form['edit_restaurant']
        session.add(restaurant)
        session.commit()
        flash('Updated '+restaurant.name+'!')
        return redirect(url_for('restaurants'))
    else:
        return render_template('editRestaurant.html', restaurant=restaurant)


# delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        # delete restaurant and menu(if exist)
        session.delete(restaurant)
        try:
            menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).one()
            session.delete(menu)
        except exc.NoResultFound:
            pass
        session.commit()
        flash('Restaurant Deleted!')
        return redirect(url_for('restaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurant)


# restaurant menu principal (all menu items)
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def menuRestaurant(restaurant_id):
    try:
        menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        return render_template('menu.html', menu=menu, restaurant=restaurant)
    # exception when no restaurant was found (restaurant_id not exist)
    except exc.NoResultFound:
        return render_template('pageNotFound.html')


# add a new menu item
@app.route('/restaurants/<int:restaurant_id>/menu/new',methods=['GET','POST'])
def newMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if '$' in request.form['new_price']:
            price = request.form['new_price']
        else:
            price = '$'+ request.form['new_price']
        
        new_item = MenuItem(name=request.form['new_name'],
                             description=request.form['new_description'],
                             price=price,
                             course=request.form['new_course'],
                             restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        
        return redirect(url_for('menuRestaurant',restaurant_id=restaurant_id))
    else:
        return render_template('newMenu.html', restaurant_id=restaurant_id,restaurant=restaurant)


# edit a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menuitem_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=menuitem_id).one()
    # check if menu item belong to the restaurant and request POST
    if restaurant_id == item.restaurant_id and request.method == 'POST':
        # change the actual value only if exist
        if request.form['item_name'] != '':
            item.name = request.form['item_name']
        if request.form['item_description'] != '':
            item.description = request.form['item_description']
        if request.form['item_price'] != '':
            if '$' in request.form['item_price']:
                item.price = request.form['item_price']
            else:
                item.price = '$'+request.form['item_price']
        if request.form['item_course'] != '':
            item.course = request.form['item_course']

        session.add(item)
        session.commit()
        return redirect(url_for('menuRestaurant',restaurant_id=restaurant_id))
    
    # when MenuItem(restaurant_id) is different of Restaurant(id)
    elif restaurant_id != item.restaurant_id:
        return "out of boundaries"
    else:
        return render_template('editMenuItem.html', restaurant=restaurant, item=item)


# delete a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/delete', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menuitem_id):
    item = session.query(MenuItem).filter_by(id=menuitem_id).one()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one() 
    if restaurant_id == item.restaurant_id and request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('menuRestaurant', restaurant_id=restaurant.id))
    elif restaurant_id != item.restaurant_id:
        return "out of boundaries"
    else:
        return render_template('deleteMenuItem.html', restaurant=restaurant, item=item)


if __name__ == "__main__":

    # to create season for users (used for flash messages)
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
