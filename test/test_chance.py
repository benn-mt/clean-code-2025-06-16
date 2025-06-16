import unittest
from src.chance import Chance

class TestChance(unittest.TestCase):
    def test_chances_are_equal_if_created_with_equal_likelihoods(self):
        self.assertEqual(Chance(1),Chance(1))
        self.assertNotEqual(Chance(1),Chance(0))

if __name__ == '__main__':
    unittest.main()