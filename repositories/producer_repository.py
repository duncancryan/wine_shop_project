from db.run_sql import run_sql
from models.producer import Producer
from models.product import Product

# start with basic CRUD, then pseudocode logic to allow filtered views

def save(producer):
    sql = "INSERT INTO producers (name, country, contact_number, contact_email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [producer.name, producer.country, producer.contact_number, producer.contact_email]
    results = run_sql(sql, values)
    id = results[0]['id']
    producer.id = id
    return producer
    