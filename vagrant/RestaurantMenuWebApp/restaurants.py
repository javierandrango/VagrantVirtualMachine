from flask import Flask, render_template
app = Flask(__name__)


# home page
@app.route('/')
@app.route('/restaurants/')
def restaurants():
    return "home page"


# add a new restaurant
@app.route('/restaurants/new/')
def newRestaurants():
    return "add new restaurant"


# edit a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return "edit a restaurant"


# delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "delete a restaurant"


# restaurant menu principal (all menu items)
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def menu(restaurant_id):
    return "restaurant menu"


# add a new menu restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenu(restaurant_id):
    return "add a new menu restaurant"


# edit a menu item 
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/edit')
def editMenuItem(restaurant_id,menuitem_id):
    return "edit a specific menu item"


# delete a menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/delete')
def deleteMenuItem(restaurant_id,menuitem_id):
    return "delete a specific menu item"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
