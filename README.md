# wine_shop_project
My first project: Admin/inventory software for an independent wine shop built using Python, Flask, SQL, psql, HTML and CSS

Technologies used: Python3, Flask (and Jinja2), PostgreSQL, psycopg2, html and CSS

In order to run the application locally: 

If you are not familiar with Python's virtual environment capacity:

- make sure that the above technologies are installed.
- download the code, and enter the working directory
- drop, then create the database and connect the sql file to it with the following commands:

    - dropdb wine_shop
    - createdb wine_shop
    - psql -d wine_shop -f db/wine_shop.sql

- if you wish to seed the database with a few items before running the app (as opposed to using the create routes in the application) run the command:
    - python3 console.py

- to launch the application:
    - flask run
    - the application should run at localhost:5000


If you are familiar with virtual environment:

- create a virtual environment with the command "python3 -m venv venv"
- to install the correct dependencies run "pip3 install -r requirements.txt"
- You will still need to have PostgreSQL installed on your system and will need to drop and create the wine_shop database as specified above, then connect it with the following commands:

    - dropdb wine_shop
    - createdb wine_shop
    - psql -d wine_shop -f db/wine_shop.sql

- run the application as before with "flask run"
- it should be running at localhost:5000.

The following outlines the brief for the MVP for this project:

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

MVP:
- The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
- The inventory should track manufacturers, including a name and any other appropriate details.
- The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
    - This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
- Show an inventory page, listing all the details for all the products in stock in a single view.
- As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.
