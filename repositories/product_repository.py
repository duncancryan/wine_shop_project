from db.run_sql import run_sql
from models.product import Product
from models.producer import Producer
import repositories.producer_repository as producer_repository

# start with basic CRUD, then pseudocode logic to allow filtered views

def save(product):
    sql "INSERT INTO products (name, type, cost, price, case_price, stock, producer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.type, product.cost, product.price, product.case_price, product.stock, product.producer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM PRODUCTS"
    results = run_sql(sql)
    for row in results:
        producer = producer_repository.select(row['producer_id'])
        product = Product(row['name'], row['type'], row['cost'], row['price'], row['case_price'], row['stock'], row['id'])
        products.append(product)
    return products