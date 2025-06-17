import unittest
from src.Measurement.quantity import Quantity

class TestQuantity(unittest.TestCase):
    def test_quantities_are_equal(self):
        self.assertEqual(Quantity(1, "Teaspoon"),Quantity(1, "Teaspoon"))