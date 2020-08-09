from flask import Flask, Blueprint, render_template, request, redirect
from controllers.product_controller import products_blueprint
from controllers.producer_controller import producers_blueprint
app = Flask(__name__)
app.register_blueprint(products_blueprint)
app.register_blueprint(producers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)