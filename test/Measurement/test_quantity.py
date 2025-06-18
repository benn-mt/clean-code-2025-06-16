import unittest
from src.Measurement.quantity import Quantity
from src.Measurement.volumes import Volume
from src.Measurement.lengths import Length

class TestQuantity(unittest.TestCase):
    def test_quantities_are_equal(self):
        self.assertEqual(Quantity(1, Volume.TEASPOON),Quantity(1, Volume.TEASPOON))
        self.assertNotEqual(Quantity(2, Volume.TEASPOON),Quantity(1, Volume.TEASPOON))
        self.assertNotEqual(Quantity(1, Volume.TEASPOON),Quantity(1, Volume.TABLESPOON))
        self.assertEqual(Quantity(1, Volume.TABLESPOON), Quantity(3, Volume.TEASPOON))

    def test_can_add_quantities(self):
        self.assertEqual(Volume.TEASPOON.s(1).add(Volume.TEASPOON.s(1)), Volume.TEASPOON.s(2))
        self.assertEqual(Volume.TABLESPOON.s(1).add(Volume.TEASPOON.s(3)), Volume.TEASPOON.s(6))
        self.assertEqual(Volume.TABLESPOON.s(1).add(Volume.TABLESPOON.s(1)), Volume.TEASPOON.s(6))
        self.assertEqual(Volume.TABLESPOON.s(1).add(Volume.TABLESPOON.s(1)), Volume.TABLESPOON.s(2))

    def test_can_not_add_quantities_with_incompatible_units(self):
        with self.assertRaises(Exception) as context:
            Quantity(1, Volume.TEASPOON).add(Quantity(1, Length.INCH))

    def test_quantities_with_incompatible_units_are_not_equal(self):
        self.assertNotEqual(Quantity(1, Volume.TEASPOON),Quantity(1, Length.INCH))
        self.assertNotEqual(Quantity(1, Length.INCH),Quantity(1, Volume.TEASPOON))