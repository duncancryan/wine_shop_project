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

@producers_blueprint.route("/producers/<id>")
def show_producer(id):
    producer = producer_repository.select(id)
    return render_template("producers/show.html", producer=producer)

@producers_blueprint.route("/producers/new")
def new_producer():
    producers = producer_repository.select_all()
    return render_template("producers/new.html", producers=producers)

@producers_blueprint.route("/producers", methods=['POST'])
def create_producer():
    name = request.form['name']
    country = request.form['country']
    contact_number = request.form['contact-number']
    contact_email = request.form['contact-email']
    new_producer = Producer(name, country, contact_number, contact_email)
    producer_repository.save(new_producer)
    return redirect("/producers")
