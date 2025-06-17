import unittest
from src.chance import Chance

CERTAIN = Chance(1)
IMPOSSIBLE = Chance(0)
FIFTY_FIFTY = Chance(0.5)

class TestChance(unittest.TestCase):
    def test_chances_are_equal_if_created_with_equal_likelihoods(self):
        self.assertEqual(Chance(1),Chance(1))
        self.assertNotEqual(Chance(1),Chance(0))

    def test_not_is_inverse_of_probablility(self):
        self.assertEqual(FIFTY_FIFTY, FIFTY_FIFTY.not_())
        self.assertEqual(CERTAIN, IMPOSSIBLE.not_())
        self.assertEqual(IMPOSSIBLE, IMPOSSIBLE.not_().not_())
        self.assertEqual(Chance(0.4).not_(), Chance(0.6))
        self.assertEqual(Chance(1.0 / 3.0).not_(), Chance(2.0 / 3.0))

    def test_can_be_combined_with_and(self):
        self.assertEqual(CERTAIN.and_(CERTAIN), CERTAIN)
        self.assertEqual(CERTAIN.and_(IMPOSSIBLE), IMPOSSIBLE)
        self.assertEqual(CERTAIN.and_(FIFTY_FIFTY), FIFTY_FIFTY)
        self.assertEqual(FIFTY_FIFTY.and_(FIFTY_FIFTY), Chance(0.25))

    def test_can_be_combined_with_or(self):
        self.assertEqual(CERTAIN.or_(CERTAIN), CERTAIN)
        self.assertEqual(FIFTY_FIFTY.or_(FIFTY_FIFTY), Chance(0.75))
        self.assertEqual(FIFTY_FIFTY.or_(CERTAIN), CERTAIN)
        self.assertEqual(IMPOSSIBLE.or_(FIFTY_FIFTY), FIFTY_FIFTY)


if __name__ == '__main__':
    unittest.main()