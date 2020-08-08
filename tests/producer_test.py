import unittest
from models.producer import Producer

class TestProducer(unittest.TestCase):
    def setUp(self):
        self.producer = Producer("Black Friars Distillery", "UK", "01752 665 292", "info@plymouthdistillery.com")