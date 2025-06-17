import unittest
from src.Measurement.quantity import Quantity
from src.Measurement.volumes import Volume

class TestQuantity(unittest.TestCase):
    def test_quantities_are_equal(self):
        self.assertEqual(Quantity(1, Volume.TABLESPOON), Quantity(3, Volume.TEASPOON))
        self.assertEqual(Quantity(1, Volume.OUNCE), Quantity(2, Volume.TABLESPOON))