from flask import Flask, Blueprint, render_template, request, redirect
import repositories.product_repository as product_repository
import repositories.producer_repository as producer_repository
from models.product import Product
from models.producer import Producer

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template('/products/index.html', products=products)

@products_blueprint.route("/products/<id>")
def show_product(id):
    product = product_repository.select(id)
    individual_markup = product.calculate_markup_individual()
    case_markup = product.calculate_markup_case()
    return render_template("/products/show.html", product=product, individual_markup=individual_markup, case_markup=case_markup)

@products_blueprint.route("/products/new")
def new_product():
    producers = producer_repository.select_all()
    return render_template("products/new.html", producers=producers)    

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    name = request.form['name']
    type = request.form['type']
    producer_id = request.form['producer-id']
    producer = producer_repository.select(producer_id)
    cost = request.form['cost']
    price = request.form['price']
    case_price = request.form['case-price']
    stock = request.form['stock']
    new_product = Product(name, type, producer, cost, price, case_price, stock)
    product_repository.save(new_product)
    return redirect("/products")

@products_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    producers = product_repository.select_all()
    return render_template("products/edit.html", product=product, producers=producers)

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")

