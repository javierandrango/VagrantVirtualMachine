from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        return redirect(url_for('restaurants'))
    else:
        return render_template('editRestaurant.html', restaurant=restaurant)


# delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurant)
        return redirect(url_for('restaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurant)


# restaurant menu principal (all menu items)
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def menuRestaurant(restaurant_id):
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    return render_template('menu.html', menu=menu, restaurant=restaurant)


# add a new menu restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenu(restaurant_id):
    return render_template('newMenu.html',
                           restaurant_id=restaurant_id)


# edit a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/edit')
def editMenuItem(restaurant_id, menuitem_id):
    return render_template('editMenuItem.html',
                           restaurant_id=restaurant_id,
                           menuitem_id=menuitem_id)


# delete a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/delete')
def deleteMenuItem(restaurant_id, menuitem_id):
    return render_template('deleteMenuItem.html',
                           restaurant_id=restaurant_id,
                           menuitem_id=menuitem_id)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
