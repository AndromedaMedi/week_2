import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Beer", 3.50, 3)
    
    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)

     