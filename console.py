import pdb
from models.product import Product
from models.producer import Producer
import repositories.product_repository as product_repository
import repositories.producer_repository as producer_repository

product_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("Black Friars Distillery", "UK", "01752 665 292", "info@plymouthdistillery.com")
producer_repository.save(producer1)
producer2 = Producer("Newton Johnson", "South Africa", "+27283123862", "wine@newtonjohnson.com")
producer_repository.save(producer2)
producer3 = Producer("Ataraxia", "South Africa", "+2345678910", "wine@ataraxia.com")
producer_repository.save(producer3)
product1 = Product("Plymouth Gin", "Gin", producer1, 10.50, 22.00, 115.00, 43, )
product_repository.save(product1)
product2 = Product("Newton Johnson Pinot Noir 2015", "Red Wine", producer2, 8.50, 18.95, 107.50, 34)
product_repository.save(product2)
product3 = Product("Newton Johnson Syrah Grenache 2018", "Red Wine", producer2, 6.80, 14.50, 80.00, 54)
product_repository.save(product2)

producers = producer_repository.select_all()
print(producers)
products = product_repository.select_all()
print(products)

product2.name = "Full Stop Rock 2016"
product_repository.update(product2)
producer1.name = "Plymouth Distillery"
producer_repository.update(producer1)

countries = producer_repository.get_countries_distinct()
print(countries)
sa_producers = producer_repository.select_country("South Africa")
sa_01 = sa_producers[0]
sa_02 = sa_producers[1]
print(sa_01.name)
print(sa_02.name)
sa_01.mark_inactive()
producer_repository.update(sa_01)

nj_wines = product_repository.select_producer(producer2)
nj_01 = nj_wines[0]
nj_02 = nj_wines[1]
print(nj_01.name)
print(nj_02.name)

red_wines = product_repository.select_type("Red Wine")
rw_1 = red_wines[0]
rw_2 = red_wines[1]
print(rw_1.name)
print(rw_2.name)

rw_1.reduction = 50
rw_1.enact_reduction()

pdb.set_trace()