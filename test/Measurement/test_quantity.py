import unittest
from src.Measurement.quantity import Quantity
from src.Measurement.volumes import Volume

class TestQuantity(unittest.TestCase):
    def test_quantities_are_equal(self):
        self.assertEqual(Quantity(1, Volume.TEASPOON),Quantity(1, Volume.TEASPOON))
        self.assertNotEqual(Quantity(2, Volume.TEASPOON),Quantity(1, Volume.TEASPOON))
        self.assertNotEqual(Quantity(1, Volume.TEASPOON),Quantity(1, Volume.TABLESPOON))
        
        self.assertEqual(Quantity(1, Volume.TABLESPOON), Quantity(3, Volume.TEASPOON))