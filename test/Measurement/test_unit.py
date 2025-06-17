import unittest
from src.Measurement.unit import Unit

class TestUnit(unittest.TestCase):
    def test_units_are_equal(self):
        UNIT1 = Unit()
        self.assertEqual(UNIT1, UNIT1)
        self.assertNotEqual(UNIT1, Unit())

    def test_returns_converted_amount(self):
        UNIT1 = Unit(3)
        self.assertEqual(UNIT1.amountInBaseUnit(3), 9)
        self.assertEqual(UNIT1.amountInBaseUnit(4), 12)
        UNIT2 = Unit(2)
        self.assertEqual(UNIT2.amountInBaseUnit(3), 6)