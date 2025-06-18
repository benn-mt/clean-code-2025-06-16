import unittest
from src.Measurement.unit import Unit

class TestUnit(unittest.TestCase):
    def test_units_are_equal(self):
        UNIT1 = Unit()
        self.assertEqual(UNIT1, UNIT1)
        self.assertNotEqual(UNIT1, Unit())

    def test_can_calculate_amount_in_relative_unit(self):
        myBaseUnit = Unit()
        mySecondUnit = Unit(2,myBaseUnit)
        myThirdUnit = Unit(3, mySecondUnit)
        self.assertEqual(myBaseUnit.amountInUnit(1, myBaseUnit), 1)
        self.assertEqual(myBaseUnit.amountInUnit(4, mySecondUnit), 2)
        self.assertEqual(mySecondUnit.amountInUnit(3, myBaseUnit), 6)
        self.assertEqual(myThirdUnit.amountInUnit(1, myBaseUnit), 6)
        self.assertEqual(myThirdUnit.amountInUnit(1, mySecondUnit), 3)

    def test_units_are_compatible_if_same_base(self):
        myBaseUnit = Unit()
        self.assertTrue(myBaseUnit.isCompatibleWith(myBaseUnit))
        myOtherBaseUnit = Unit()
        self.assertFalse(myBaseUnit.isCompatibleWith(myOtherBaseUnit))
        mySecondUnit = Unit(2, myBaseUnit)
        self.assertTrue(myBaseUnit.isCompatibleWith(mySecondUnit))
        myOtherSecondUnit = Unit(2, myOtherBaseUnit)
        self.assertFalse(myOtherSecondUnit.isCompatibleWith(mySecondUnit))
        myThirdUnit = Unit(2, mySecondUnit)
        self.assertTrue(myBaseUnit.isCompatibleWith(myThirdUnit))