import unittest
from models.product import Product
from models.producer import Producer

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.producer = Producer("Black Friars Distillery", "UK", "01752 665 292", "info@plymouthdistillery.com")
        self.product = Product("Plymouth Gin", "Gin", self.producer, 10.50, 22.00, 115.00, 43)
