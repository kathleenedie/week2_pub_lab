import unittest
from src.customer import Customer

class TestCustomer (unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Ian", 50)

    def test_customer_has_money(self):
        self.assertEqual = (50, self.customer)