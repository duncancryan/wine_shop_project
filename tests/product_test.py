import unittest
from models.product import Product
from models.producer import Producer

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.producer = Producer("Black Friars Distillery", "UK", "01752 665 292", "info@plymouthdistillery.com")
        self.product = Product("Plymouth Gin", "Gin", self.producer, 10.50, 22.00, 115.00, 43)

    def test_product_has_name(self):
        self.assertEqual("Plymouth Gin", self.product.name)
    
    def test_product_has_type(self):
        self.assertEqual("Gin", self.product.type)
    
    def test_product_has_producer(self):
        self.assertEqual(self.producer, self.product.producer)
    
    def test_producer_can_be_accessed(self):
        self.assertEqual("Black Friars Distillery", self.product.producer.name)

    def test_product_has_cost(self):
        self.assertEqual(10.50, self.product.cost)
    
    def test_product_has_price(self):
        self.assertEqual(22.00, self.product.price)
    
    def test_product_has_case_price(self):
        self.assertEqual(115.00, self.product.case_price)