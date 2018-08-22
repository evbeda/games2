import unittest
from throwDice import throwDice


class TestThrowDice(unittest.TestCase):
    def test_throw(self):
        throwResult = throwDice(1)
        self.assertTrue(1 <= throwResult[0] <= 6)


if __name__ == '__main__':
    unittest.main()
