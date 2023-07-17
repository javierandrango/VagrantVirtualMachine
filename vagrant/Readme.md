# Introduction
Vagrant Virtual Machine directory.
Any file inside this directory `/vagrant` is shared with the `vagrant` folder on your computer. This means that you can edit code in your favorite text editor, and run it inside the VM. The PostgreSQL database itself lives only inside the VM.

# Results
Projects inside the vagrant shared folder:

## 1. `newsdata`
python DataBase-API: 

**Internal reporting tool** that will use information from a database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code answer questions about the site's user activity.
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

An HTML file was created to present the report.

## 2. `RestaurantMenuWebApp`
Web application using the Flask framework and SQLAlchemy to manage a database of restaurants and their menus.
The application:
1. creates new restaurants (new element into the DB)
2. edit/delete restaurants 
3. creates a new restaurant menu item
4. edit/delete restaurant menu item
5. show restaurant information in JSON format
6. show restaurant menu information in JSON format
7. show single menu item information in JSON format



# Mainteners
The content described belongs to the owner of this repository and was developed for educational purposes only. files and code were generated from scratch following online guides and basic instructions from other repositories.
