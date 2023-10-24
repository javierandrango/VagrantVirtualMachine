# Prerequsites
1. Python package `sqlalchemy`:
    ```bash
    pip3 install sqlalchemy --user
    ```
2. (Optional to make direct queries) SQL Data Base engine `sqlite3`:
    ```bash
    sudo apt install sqlite3
    sqlite3 --version
    ```
3. download the DB python file from source(Udacity):
https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson_1/lotsofmenus.py
pip3
# Description:
1. Data Base:
  
| Table 1 | Table 2 |
|:---:|---|
|<table style="border-collapse:collapse;border-color:#ccc;border-spacing:0" class="tg"><thead><tr><th style="background-color:#f0f0f0;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">Restaurant</th></tr></thead><tbody><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">name (varchar)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">id (primary key)</td></tr></tbody></table>       |<table style="border-collapse:collapse;border-color:#ccc;border-spacing:0" class="tg"><thead><tr><th style="background-color:#f0f0f0;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">MenuItem</th></tr></thead><tbody><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">name (varchar)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">id (primary key)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">description (varchar)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">price (varchar)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">course (varchar)</td></tr><tr><td style="background-color:#fff;border-color:#000000;border-style:solid;border-width:1px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">restaurant_id (foreign key Restaurant.id)</td></tr></tbody></table>       |


2. Routes:

| **URL** | **Description** |
|---|---|
| /restaurants/ | show all restaurants |
| /restaurants/new | create a new restaurant |
| /restaurants/restaurant_id/edit/ | edit the name of a restaurant |
| /restaurants/restaurant_id/delete/ | delete a restaurant (included the menu items) |
| /restaurants/restaurant_id/ /restaurant/restaurant_id/menu/ | show the menu restaurant  |
| /restaurants/restaurant_id/menu/menu_item_id/edit/ | edit a restaurant menu item |
| /restaurants/restaurant_id/menu/menu_item_id/delete/ | delete a restaurant menu item |
    
3. EndPoints:

| **API Endpoints** |
|---|
| /restaurants/JSON |
| /restaurants/restaurant_id/menu/JSON |
| /restaurants/restaurant_id/menu/menu_item_id/JSON |

# Usage
1. Create the Database through Python and add items: 
    ```bash
    python3 database_setup.py
    python3 lotsofmenus.py 
    ```
2. Run the Python aplication `restaurants.py`:
    ```bash
    python3 restaurants.py
    ```
3. Open a Chrome web Broser and access the app with URL:
    ```URL
    localhost:5000/
    localhost:5000/restaurants
    ```
# Updates
1. 17/07/2023 : First version added CSS and some Javascript, the responsive design for the web application was tested only for `mobile phones`. 

    (NOTE:) I found an error when sending an empty string while creating a new restaurant or an item menu.(Future Validation)
