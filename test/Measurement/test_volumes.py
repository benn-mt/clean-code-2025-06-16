import unittest
from src.Measurement.quantity import Quantity
from src.Measurement.volumes import Volume

class TestQuantity(unittest.TestCase):
    def test_quantities_are_equal(self):
        self.assertEqual(Quantity(1, Volume.TABLESPOON), Quantity(3, Volume.TEASPOON))
        self.assertEqual(Quantity(1, Volume.OUNCE), Quantity(2, Volume.TABLESPOON))
        self.assertEqual(Quantity(1, Volume.CUP), Quantity(8, Volume.OUNCE))
        self.assertEqual(Quantity(1, Volume.PINT), Quantity(2, Volume.CUP))
        self.assertEqual(Quantity(1, Volume.QUART), Quantity(2, Volume.PINT))
        self.assertEqual(Quantity(1, Volume.GALLON), Quantity(4, Volume.QUART))

        self.assertEqual(Quantity(1, Volume.GALLON), Quantity(768, Volume.TEASPOON))

    def test_examples_from_exercise_with_s_method(self):
        self.assertEqual(Volume.TABLESPOON.s(1), Volume.TEASPOON.s(3))
        self.assertEqual(Volume.OUNCE.s(1), Volume.TABLESPOON.s(2))
        self.assertEqual(Volume.CUP.s(1), Volume.OUNCE.s(8))
        self.assertEqual(Volume.PINT.s(1), Volume.CUP.s(2))
        self.assertEqual(Volume.QUART.s(1), Volume.PINT.s(2))
        self.assertEqual(Volume.GALLON.s(1), Volume.QUART.s(4))