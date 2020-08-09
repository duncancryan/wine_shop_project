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
product1 = Product("Plymouth Gin", "Gin", producer1, 10.50, 22.00, 115.00, 43)
product_repository.save(product1)
product2 = Product("Newton Johnson Pinot Noir 2015", "Red Wine", producer2, 8.50, 18.95, 107.50, 34)
product_repository.save(product2)

producers = producer_repository.select_all()
print(producers)
products = product_repository.select_all()
print(products)

product2.name = "Full Stop Rock 2016"
product_repository.update(product2)
producer1.name = "Plymouth Distillery"
producer_repository.update(producer1)

pdb.set_trace()