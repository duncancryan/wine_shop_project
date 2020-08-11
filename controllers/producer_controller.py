from flask import Flask, Blueprint, render_template, request, redirect
import repositories.product_repository as product_repository
import repositories.producer_repository as producer_repository
from models.product import Product
from models.producer import Producer

producers_blueprint = Blueprint("producers", __name__)

@producers_blueprint.route("/producers")
def producers():
    producers = producer_repository.select_all()
    countries = producer_repository.get_countries_distinct()
    return render_template("producers/index.html", producers=producers, countries=countries)

@producers_blueprint.route("/producers/<id>")
def show_producer(id):
    producer = producer_repository.select(id)
    products = producer_repository.products(producer)
    return render_template("producers/show.html", producer=producer, products=products)

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

@producers_blueprint.route("/producers/<id>/edit")
def edit_producer(id):
    producer = producer_repository.select(id)
    return render_template("/producers/edit.html", producer=producer)

@producers_blueprint.route("/producers/<id>", methods=['POST'])
def update_producer(id):
    name = request.form["name"]
    country = request.form["country"]
    contact_number = request.form['contact-number']
    contact_email = request.form['contact-email']
    producer = Producer(name, country, contact_number, contact_email, id)
    producer_repository.update(producer)
    return redirect("/producers")

@producers_blueprint.route("/producers/<id>/delete", methods=['POST'])
def delete_producer(id):
    producer_repository.delete(id)
    return redirect("/producers")

@producers_blueprint.route("/producers/<country>/")
def by_country(country):
    local_producers = producer_repository.select_country(country)
    return render_template("/producers/country.html", local_producers=local_producers)