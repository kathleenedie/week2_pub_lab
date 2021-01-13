import unittest
from src.customer import Customer

class TestCustomer (unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Ian", 50, 73)

    def test_customer_has_money(self):
        self.assertEqual = (50, self.customer)
    
    def test_customer_spends_money(self):
        self.customer.customer_spends_money(2.50)
        self.assertEqual = (47.50, self.customer)