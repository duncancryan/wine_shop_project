from flask import Flask, Blueprint, render_template, request, redirect
import repositories.product_repository as product_repository
import repositories.producer_repository as producer_repository
from models.product import Product
from models.producer import Producer

producers_blueprint = Blueprint("producers", __name__)

@producers_blueprint.route("/producers")
def producers():
    producers = producer_repository.select_all()
    return render_template("producers/index.html", producers=producers)