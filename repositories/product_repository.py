from db.run_sql import run_sql
from models.product import Product
from models.producer import Producer
import repositories.producer_repository as producer_repository

# start with basic CRUD, then pseudocode logic to allow filtered views

def save(product):
    sql = "INSERT INTO products (name, type, cost, price, case_price, stock, producer_id, reduction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.type, product.cost, product.price, product.case_price, product.stock, product.producer.id, product.reduction]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        producer = producer_repository.select(row['producer_id'])
        product = Product(row['name'], row['type'], producer, row['cost'], row['price'], row['case_price'], row['stock'], row['reduction'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        producer = producer_repository.select(result['producer_id'])
        product = Product(result['name'], result['type'], producer, result['cost'], result['price'], result['case_price'], result['stock'], result['reduction'], result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, type, cost, price, case_price, stock, producer_id, reduction) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.type, product.cost, product.price, product.case_price, product.stock, product.producer.id, product.reduction, product.id]
    run_sql(sql, values)

def select_producer(producer):
    products = []
    sql = "SELECT * FROM products WHERE producer_id = %s"
    values = [producer.id]
    results = run_sql(sql, values)
    for row in results:
        product = Product(row['name'], row['type'], producer, row['cost'], row['price'], row['case_price'], row['stock'], row['reduction'], row['id'])
        products.append(product)
    return products

def get_distinct_types():
    types = []
    sql = "SELECT DISTINCT type FROM products"
    results = run_sql(sql)
    for row in results:
        type = row[0]
        types.append(type)
    return types

def select_type(type):
    products =[]
    sql = "SELECT * FROM products WHERE type = %s"
    values = [type]
    results = run_sql(sql, values)
    for row in results:
        producer = producer_repository.select(row['producer_id'])
        product = Product(row['name'], row['type'], producer, row['cost'], row['price'], row['case_price'], row['stock'], row['reduction'], row['id'])
        products.append(product)
    return products

def low_stock():
    products = []
    sql = "SELECT * FROM products WHERE stock < 10"
    results = run_sql(sql)
    for row in results:
        producer = producer_repository.select(row['producer_id'])
        product = Product(row['name'], row['type'], producer, row['cost'], row['price'], row['case_price'], row['stock'], row['reduction'], row['id'])
        products.append(product)
    return products