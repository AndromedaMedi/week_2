import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

        self.drink1 = Drink("Beer", 3.50, 2)
        self.drink2 = Drink("Wine", 4.00, 4)
        self.drink3 = Drink("Rum", 4.50, 5)

        self.customer1 = Customer("Dave", 20.00, 32, 2)
        self.customer2 = Customer("Jane", 10.00, 21, 5)
        self.customer3 = Customer("Joe", 3.00, 15, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_a_till(self):    
        self.assertEqual(100.00, self.pub.till)
 
    def test_increase_till(self):
        self.pub.increase_till(3.50)
        self.assertEqual(103.50, self.pub.till)

    # def test_pub_stock_value_starts_at_0(self):
    #     self.assertEqual(None, self.pub.stock_value())

    # def test_stock_level_0_if_drink_not_in_stock(self):
    #     self.assertEqual(0, self.pub.stock_level())

    # def test_pub_can_add_drink(self):
    #     self.pub.add_drink(self.drink1)
    #     self.assertEqual(1, self.pub.stock_level(self.drink1))
    #     self.assertEqual(1, self.pub.stock_value())
    
    def test_can_sell_drink_to_customer(self):
        drink_price = Drink("Beer", 3.50, 2)
        self.pub.sell_drink_to_customer("Beer", self.customer1)
        self.customer1.reduce_money(self.drink1.price)
        self.pub.increase_till(drink_price)
        self.assertEqual(16.50, self.customer1.wallet)
        self.assertEqual(103.50, self.pub.till)
    

