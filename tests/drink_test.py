import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("wine", 4.00, 5, 10)
        
    
    def test_drink_has_name(self):
        self.assertEqual("wine", self.drink.name)
    
    def test_has_alcohol_level(self):
        self.assertEqual(5, self.drink.alcohol_level)

    def test_drink_has_stock_level(self):
        self.assertEqual(10, self.drink.stock_level)