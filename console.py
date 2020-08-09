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

pdb.set_trace()