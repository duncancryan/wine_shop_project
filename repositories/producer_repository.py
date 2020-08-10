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

# Next, I need to create a function which queries the database and identifies producers by country
# I can then call this in the controller to create filtering features for the list of producers

def select_country(country):
    # will need an empty list to put results in
    producers = []
    # sql will need to be SELECT FROM with a WHERE clause for country
    sql = "SELECT FROM producers WHERE country = %s"
    # values will be the country being passed in
    # this will need to be in single quotes here I think, to fit the sql?
    values = ['country']
    # multiple possible results, so results and then a for loop
    results = run_sql(sql, values)
    for row in results:
        producer = Producer(row['name'], row['country'], row['contact_number'], row['contact_email'], row['id'])
        producers.append(producer)
    return producers
