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
    return render_template("/products/show.html", product=product)

# @products_blueprint.route("/products/<id>/edit")
# def edit_product(id):
#     producers = producer_repository.select_all()
#     return render_template("p")    