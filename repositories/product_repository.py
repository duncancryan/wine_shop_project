from db.run_sql import run_sql
from models.product import Product
from models.producer import Producer
import repositories.producer_repository as producer_repository

# start with basic CRUD, then pseudocode logic to allow filtered views

def save(product):
    sql = "INSERT INTO products (name, type, cost, price, case_price, stock, producer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
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
        product = Product(row['name'], row['type'], producer, row['cost'], row['price'], row['case_price'], row['stock'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        producer = producer_repository.select(result['producer_id'])
        product = Product(result['name'], result['type'], producer, result['cost'], result['price'], result['case_price'], result['stock'], result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, type, cost, price, case_price, stock, producer_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.type, product.cost, product.price, product.case_price, product.stock, product.producer.id, product.id]
    run_sql(sql, values)

