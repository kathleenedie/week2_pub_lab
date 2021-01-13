import unittest
from src.drinks import Drinks

class TestDrinks (unittest.TestCase):
    
    def setUp(self):
        self.drinks = Drinks("rum", 3.20)
    
    def test_drink_has_price(self):
        self.assertEqual = (3.20, self.drinks.price)