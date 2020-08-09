from flask import Flask, Blueprint, render_template, request, redirect
import repositories.product_repository as product_repository
import repositories.producer_repository as producer_repository
from models.product import Product
from models.producer import Producer

products_blueprint = Blueprint("products", __name__)