import unittest
from src.customer import Customer
from src.drink import Drink 

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Dave", 20.00, 32, 2)
        self.drink = Drink("Beer", 3.50, 3)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_customer_has_drunkeness(self):
        self.assertEqual(2, self.customer.drunkeness)

    def test_customer_had_age(self):
        self.assertEqual(32, self.customer.age)
    
    def test_customer_can_buy_drink(self):
        drink = Drink("beer", 3.50, 3)
        self.customer.buy_drink(drink)
        self.assertEqual(16.50, self.customer.wallet)

    def test_cutomer_reduce_money(self):
        self.customer.reduce_money(3.50)
        self.assertEqual(16.50, self.customer.wallet)