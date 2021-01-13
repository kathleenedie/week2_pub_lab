import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub (unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual ("The Prancing Pony", self.pub.name)

    def test_increase_in_till(self):
        self.pub.increase_in_till(2.50)
        self.assertEqual (102.50, self.pub.total_cash)

    def test_drink_purchase_till(self):
        customer = Customer("Jimmy Punter", 10.00, 25)
        self.pub.drink_purchase(customer, 4)
        self.assertEqual (104.00, self.pub.total_cash)
        self.assertEqual (6.00, customer.wallet)

    def test_check_customer_age_over(self):
        customer = Customer("Lulu McHugh", 20.00, 21)
        self.pub.check_customer_age(customer)
        self.assertEqual (True, self.pub.check_customer_age(customer))

    def test_check_customer_age_under(self):
        customer = Customer("Caeden McGillicuddy", 5.50, 17)
        self.pub.check_customer_age(customer)
        self.assertEqual (False, self.pub.check_customer_age(customer))
