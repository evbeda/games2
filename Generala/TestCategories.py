import unittest
from .utils import check_throw


class TestCategories(unittest.TestCase):

    def test_generala(self):
        numOfThrows = 2
        mockThrow = [1, 1, 1, 1, 1]
        isGenerala = check_throw(mockThrow, "generala", numOfThrows)
        self.assertTrue(isGenerala)

    def test_not_generala(self):
        numOfThrows = 2
        mockThrow = [2, 3, 1, 1, 1]
        isNotGenerala = check_throw(mockThrow, "generala", numOfThrows)
        self.assertFalse(isNotGenerala)

    def test_not_generala_is_servida(self):
        numOfThrows = 1
        mockThrow = [2, 1, 1, 1, 1]
        isNotGenerala = check_throw(mockThrow, "generalaServida", numOfThrows)
        self.assertFalse(isNotGenerala)

    def test_generala_servida(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 1, 1]
        isGeneralaServida = check_throw(mockThrow, "generalaServida", numOfThrows)
        self.assertTrue(isGeneralaServida)

    def test_not_generala_servida(self):
        numOfThrows = 2
        mockThrow = [1, 1, 1, 1, 1]
        isNotGeneralaServida = check_throw(mockThrow, "generalaServida", numOfThrows)
        self.assertFalse(isNotGeneralaServida)

    def test_poker(self):
        numOfThrows = 1
        mockThrow = [1, 5, 1, 1, 1]
        isPoker = check_throw(mockThrow, "poker", numOfThrows)
        self.assertTrue(isPoker)

    def test_not_poker(self):
        numOfThrows = 1
        mockThrow = [3, 3, 3, 1, 1]
        isNotPoker = check_throw(mockThrow, "poker", numOfThrows)
        self.assertFalse(isNotPoker)

    def test_full(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 5, 5]
        isFull = check_throw(mockThrow, "full", numOfThrows)
        self.assertTrue(isFull)

    def test_not_full(self):
        numOfThrows = 1
        mockThrow = [3, 3, 4, 1, 1]
        isNotFull = check_throw(mockThrow, "full", numOfThrows)
        self.assertFalse(isNotFull)

    def test_escalera(self):
        numOfThrows = 1
        mockThrow = [2, 3, 4, 5, 6]
        isEscalera = check_throw(mockThrow, "escalera", numOfThrows)
        self.assertTrue(isEscalera)

    def test_not_escalera(self):
        numOfThrows = 1
        mockThrow = [1, 2, 4, 5, 6]
        isNotEscalera = check_throw(mockThrow, "escalera", numOfThrows)
        self.assertFalse(isNotEscalera)

    def test_generala_doble_segunda_tercera(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 3, 4, 3, 4]
        mockThrow2 = [2, 2, 2, 2, 2]
        mockThrow3 = [4, 4, 4, 4, 4]
        isGeneralaDoble = [
            check_throw(mockThrow, "generala", numOfThrows),
            check_throw(mockThrow2, "generala", numOfThrows2),
            check_throw(mockThrow3, "generala", numOfThrows3),
        ]
        self.assertFalse(isGeneralaDoble[0])
        self.assertTrue(isGeneralaDoble[1])
        self.assertTrue(isGeneralaDoble[2])

    def test_not_generala_doble(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 3, 4, 3, 4]
        mockThrow2 = [4, 4, 4, 4, 4]
        mockThrow3 = [3, 2, 2, 2, 1]
        isNotGeneralaDoble = [
            check_throw(mockThrow, "generala", numOfThrows),
            check_throw(mockThrow2, "generala", numOfThrows2),
            check_throw(mockThrow3, "generala", numOfThrows3),
        ]
        self.assertFalse(isNotGeneralaDoble[0])
        self.assertTrue(isNotGeneralaDoble[1])
        self.assertFalse(isNotGeneralaDoble[2])

    def test_generala_doble_primera_segunda(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 1, 1, 1, 1]
        mockThrow2 = [2, 2, 2, 2, 2]
        mockThrow3 = [4, 2, 1, 4, 5]
        isGeneralaDoble = [
            check_throw(mockThrow, "generalaServida", numOfThrows),
            check_throw(mockThrow2, "generala", numOfThrows2),
            check_throw(mockThrow3, "generala", numOfThrows3),
        ]
        self.assertTrue(isGeneralaDoble[0])
        self.assertTrue(isGeneralaDoble[1])
        self.assertFalse(isGeneralaDoble[2])

    def test_generala_doble_primera_tercera(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 1, 1, 1, 1]
        mockThrow2 = [2, 2, 3, 2, 2]
        mockThrow3 = [4, 4, 4, 4, 4]
        isGeneralaDoble = [
            check_throw(mockThrow, "generalaServida", numOfThrows),
            check_throw(mockThrow2, "generala", numOfThrows2),
            check_throw(mockThrow3, "generala", numOfThrows3),
        ]
        self.assertTrue(isGeneralaDoble[0])
        self.assertFalse(isGeneralaDoble[1])
        self.assertTrue(isGeneralaDoble[2])

    def test_generala_doble_triple(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 1, 1, 1, 1]
        mockThrow2 = [2, 2, 2, 2, 2]
        mockThrow3 = [4, 4, 4, 4, 4]
        isGeneralaDoble = [
            check_throw(mockThrow, "generalaServida", numOfThrows),
            check_throw(mockThrow2, "generala", numOfThrows2),
            check_throw(mockThrow3, "generala", numOfThrows3),
        ]
        self.assertTrue(isGeneralaDoble[0])
        self.assertTrue(isGeneralaDoble[1])
        self.assertTrue(isGeneralaDoble[2])

    def test_number_one(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 4, 4]
        sumOfOnes = check_throw(mockThrow, 1, numOfThrows)
        self.assertEqual(sumOfOnes, 3)

    def test_not_number_one(self):
        numOfThrows = 1
        mockThrow2 = [5, 6, 3, 4, 2]
        sumOfOnes2 = check_throw(mockThrow2, 1, numOfThrows)
        self.assertEqual(sumOfOnes2, 0)

    def test_number_two(self):
        numOfThrows = 1
        mockThrow = [2, 2, 2, 4, 4]
        sumOfTwos = check_throw(mockThrow, 2, numOfThrows)
        self.assertEqual(sumOfTwos, 6)

    def test_not_number_two(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 1, 4]
        sumOfTwos2 = check_throw(mockThrow2, 2, numOfThrows)
        self.assertEqual(sumOfTwos2, 0)

    def test_number_three(self):
        numOfThrows = 1
        mockThrow = [3, 3, 3, 4, 2]
        sumOfThrees = check_throw(mockThrow, 3, numOfThrows)
        self.assertEqual(sumOfThrees, 9)

    def test_not_number_three(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 1, 4, 2]
        sumOfThrees2 = check_throw(mockThrow2, 3, numOfThrows)
        self.assertEqual(sumOfThrees2, 0)

    def test_number_four(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 4, 4]
        sumOfFours = check_throw(mockThrow, 4, numOfThrows)
        self.assertEqual(sumOfFours, 8)

    def test_not_number_four(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 1, 2]
        sumOfFours2 = check_throw(mockThrow2, 4, numOfThrows)
        self.assertEqual(sumOfFours2, 0)

    def test_number_five(self):
        numOfThrows = 1
        mockThrow = [1, 5, 5, 4, 4]
        sumOfFives = check_throw(mockThrow, 5, numOfThrows)
        self.assertEqual(sumOfFives, 10)

    def test_not_number_five(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 4, 2]
        sumOfFives2 = check_throw(mockThrow2, 5, numOfThrows)
        self.assertEqual(sumOfFives2, 0)

    def test_number_six(self):
        numOfThrows = 1
        mockThrow = [1, 6, 6, 4, 4]
        sumOfSixes = check_throw(mockThrow, 6, numOfThrows)
        self.assertEqual(sumOfSixes, 12)

    def test_not_number_six(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 5, 4, 2]
        sumOfSixes2 = check_throw(mockThrow2, 6, numOfThrows)
        self.assertEqual(sumOfSixes2, 0)
