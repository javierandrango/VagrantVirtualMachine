from flask import Flask, render_template
app = Flask(__name__)


# home page
@app.route('/')
@app.route('/restaurants/')
def restaurants():
    return render_template('restaurants.html')


# add a new restaurant
@app.route('/restaurants/new/')
def newRestaurant():
    return render_template('newRestaurant.html')


# edit a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html',
                           restaurant_id=restaurant_id)


# delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html',
                           restaurant_id=restaurant_id)


# restaurant menu principal (all menu items)
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def menu(restaurant_id):
    return render_template('menu.html',
                           restaurant_id=restaurant_id)


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
