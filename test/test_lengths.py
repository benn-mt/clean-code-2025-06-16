import unittest
from src.Measurement.quantity import Quantity
from src.Measurement.lengths import Length

class TestQuantity(unittest.TestCase):
    def test_examples_from_exercise_with_s_method(self):
        self.assertEqual(Length.INCH.s(12), Length.FOOT.s(1))
        self.assertEqual(Length.FOOT.s(3), Length.YARD.s(1))
        self.assertEqual(Length.YARD.s(220), Length.FURLONG.s(1))
        self.assertEqual(Length.FURLONG.s(8), Length.MILE.s(1))