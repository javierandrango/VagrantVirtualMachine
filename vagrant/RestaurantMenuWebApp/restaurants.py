from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc
from database_setup import Base, Restaurant, MenuItem
#import re # to work with regular expression (search in string. examples currency,date,etc)

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
            # try when a menu item in restaurant exist
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
    except exc.NoResultFound:
        # exception when no restaurant was found (restaurant_id not exist)
        # error only found in manual input in URL
        return render_template('pageNotFound.html')


# add a new menu item
@app.route('/restaurants/<int:restaurant_id>/menu/new',methods=['GET','POST'])
def newMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['new_name'],
                             description=request.form['new_description'],
                             price=request.form['new_price'],
                             course=request.form['new_course'],
                             restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        flash("New Item added!")
        return redirect(url_for('menuRestaurant',restaurant_id=restaurant_id))
    else:
        return render_template('newMenu.html', restaurant_id=restaurant_id,restaurant=restaurant)


# edit a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/edit/', methods=['GET','POST'])
def editMenuItem(restaurant_id, menuitem_id):
    try:
        # catch manual input from URL and query to the DB.
        # restaurant_id and menuitem_id could be any number
        # if the id cant be found in DB it will raise an exception. 
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        item = session.query(MenuItem).filter_by(id=menuitem_id).one()
        
        if restaurant_id == item.restaurant_id and request.method == 'POST':
            # change the actual value only if exist
            if request.form['item_name'] != '':
                item.name = request.form['item_name']
            if request.form['item_description'] != '':
                item.description = request.form['item_description']
            if request.form['item_price'] != '':
                item.price = request.form['item_price']
            if request.form['item_course'] != '':
                item.course = request.form['item_course']

            session.add(item)
            session.commit()
            flash("Item edited!")
            return redirect(url_for('menuRestaurant',restaurant_id=restaurant_id))
        
        # when MenuItem(restaurant_id) is different of Restaurant(id)
        elif restaurant_id != item.restaurant_id:
            return render_template('pageNotFound.html')
    except exc.NoResultFound:
        return render_template('pageNotFound.html')
    else:
        return render_template('editMenuItem.html', restaurant=restaurant, item=item)


# delete a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/delete/', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menuitem_id):
    try:
        item = session.query(MenuItem).filter_by(id=menuitem_id).one()
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        if restaurant_id == item.restaurant_id and request.method == 'POST':
            session.delete(item)
            session.commit()
            flash("item deleted!")
            return redirect(url_for('menuRestaurant', restaurant_id=restaurant.id))
        elif restaurant_id != item.restaurant_id:
            return render_template('pageNotFound.html')
    except exc.NoResultFound:
        return render_template('pageNotFound.html')
    else:
        return render_template('deleteMenuItem.html', restaurant=restaurant, item=item)


# making API Endpoints
@app.route('/restaurants/JSON/')
def jsonRestaurants():
    # show all restaurants in JSO format
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants ])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def jsonMenuRestaurant(restaurant_id):
    # show specific restaurant in JSON format
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    return {restaurant.name:jsonify([i.serialize for i in menu]).json}

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/JSON/')
def jsonMenuItem(restaurant_id, menuitem_id):
    # show an item menu in JSON format
    menu = session.query(MenuItem).filter_by(id=menuitem_id).one()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if menu.restaurant_id == restaurant_id:
        return {restaurant.name:jsonify([menu.serialize]).json}
    else:
        return render_template('pageNotFound.html')

    

if __name__ == "__main__":

    # to create season for users (used for flash messages)
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
