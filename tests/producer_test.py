import unittest
from models.producer import Producer

class TestProducer(unittest.TestCase):
    def setUp(self):
        self.producer = Producer("Black Friars Distillery", "UK", "01752 665 292", "info@plymouthdistillery.com")

    def test_producer_has_name(self):
        pass
    
    def test_producer_has_country(self):
        pass
    
    def test_producer_has_phone(self):
        pass
    
    def test_producer_has_email(self):
        pass

    def test_producer_starts_active(self):
        pass