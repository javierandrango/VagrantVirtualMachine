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