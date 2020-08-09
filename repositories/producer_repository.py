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
    
def select_all():
    producers = []
    sql = "SELECT * FROM producers"
    results = run_sql(sql)
    for row in results:
        producer = Producer(row['name'], row['country'], row['contact_number'], row['contact_email'], row['id'])
        producers.append(producer)
    return producers

def select(id):
    producer = None
    sql = "SELECT * FROM producers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        producer = Producer(result['name'], result['country'], result['contact_number'], result['contact_email'], result['id'])
    return producer

def delete_all():
    sql = "DELETE FROM producers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM producers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(producer):
    sql = "UPDATE producers SET (name, country, contact_number, contact_email) = (%s, %s, %s, %s) WHERE id = %s"
    values = [producer.name, producer.country, producer.contact_number, producer.contact_email, producer.id]
    run_sql(sql, values)