import unittest
from src.Measurement.unit import Unit

class TestUnit(unittest.TestCase):
    def test_units_are_equal(self):
        UNIT1 = Unit()
        self.assertEqual(UNIT1, UNIT1)
        self.assertNotEqual(UNIT1, Unit())