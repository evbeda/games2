import unittest
from . import *
from .utils import check_throw


class TestCategories(unittest.TestCase):

    def test_generala(self):
        numOfThrows = 2
        mockThrow = [1, 1, 1, 1, 1]
        result = check_throw(mockThrow, GENERALA['name'], numOfThrows)
        self.assertEqual(result, GENERALA['score'])

    def test_not_generala(self):
        numOfThrows = 2
        mockThrow = [2, 3, 1, 1, 1]
        result = check_throw(mockThrow, GENERALA['name'], numOfThrows)
        self.assertEqual(result, 0)

    def test_not_generala_is_servida(self):
        numOfThrows = 1
        mockThrow = [2, 1, 1, 1, 1]
        isNotGenerala = check_throw(mockThrow, GENERALA['name'], numOfThrows)
        self.assertEqual(isNotGenerala, 0)

    def test_generala_servida(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 1, 1]
        isGeneralaServida = check_throw(mockThrow, GENERALA['name'], numOfThrows)
        self.assertEqual(isGeneralaServida, GENERALASERVIDA['score'])

    def test_not_generala_servida(self):
        numOfThrows = 2
        mockThrow = [1, 1, 1, 1, 1]
        isNotGeneralaServida = check_throw(mockThrow, GENERALA['name'], numOfThrows)
        self.assertNotEqual(isNotGeneralaServida, GENERALASERVIDA['score'])

    def test_poker(self):
        numOfThrows = 1
        mockThrow = [1, 5, 1, 1, 1]
        isPoker = check_throw(mockThrow, POKER['name'], numOfThrows)
        self.assertEqual(isPoker, POKER['score'])

    def test_not_poker(self):
        numOfThrows = 1
        mockThrow = [3, 3, 3, 1, 1]
        isNotPoker = check_throw(mockThrow, POKER['name'], numOfThrows)
        self.assertEqual(isNotPoker, 0)

    def test_full(self):
        numOfThrows = 2
        mockThrow = [1, 1, 1, 5, 5]
        isFull = check_throw(mockThrow, FULL['name'], numOfThrows)
        self.assertEqual(isFull, FULL['score'])

    def test_not_full(self):
        numOfThrows = 2
        mockThrow = [3, 3, 4, 1, 1]
        isNotFull = check_throw(mockThrow, FULL['name'], numOfThrows)
        self.assertEqual(isNotFull, 0)


    def test_full_servido(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 5, 5]
        isFull = check_throw(mockThrow, FULL['name'], numOfThrows)
        self.assertEqual(isFull, FULLSERVIDO['score'])

    def test_not_full_servido(self):
        numOfThrows = 1
        mockThrow = [3, 3, 4, 1, 1]
        isNotFullServido = check_throw(mockThrow, FULL['name'], numOfThrows)
        self.assertNotEqual(isNotFullServido, FULLSERVIDO['score'])

    def test_escalera(self):
        numOfThrows = 2
        mockThrow = [2, 3, 4, 5, 6]
        isEscalera = check_throw(mockThrow, ESCALERA['name'], numOfThrows)
        self.assertEqual(isEscalera, ESCALERA['score'])

    def test_not_escalera(self):
        numOfThrows = 1
        mockThrow = [1, 2, 4, 5, 6]
        isNotEscalera = check_throw(mockThrow, ESCALERA['name'], numOfThrows)
        self.assertEqual(isNotEscalera, 0)


    def test_escalera_servida(self):
        numOfThrows = 1
        mockThrow = [2, 3, 4, 5, 6]
        isEscalera = check_throw(mockThrow, ESCALERA['name'], numOfThrows)
        self.assertEqual(isEscalera, ESCALERASERVIDA['score'])

    def test_not_escalera_servida(self):
        numOfThrows = 2
        mockThrow = [1, 2, 4, 5, 6]
        isNotEscaleraServida = check_throw(mockThrow, ESCALERA['name'], numOfThrows)
        self.assertNotEqual(isNotEscaleraServida, ESCALERASERVIDA['score'] )

    def test_generala_doble_segunda_tercera(self):
        numOfThrows = 1
        numOfThrows2 = 2
        numOfThrows3 = 3
        mockThrow = [1, 3, 4, 3, 4]
        mockThrow2 = [2, 2, 2, 2, 2]
        mockThrow3 = [4, 4, 4, 4, 4]
        isGeneralaDoble = [
            check_throw(mockThrow, GENERALA['name'], numOfThrows),
            check_throw(mockThrow2, GENERALA['name'], numOfThrows2),
            check_throw(mockThrow3, GENERALA['name'], numOfThrows3),
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
            check_throw(mockThrow, GENERALA['name'], numOfThrows),
            check_throw(mockThrow2, GENERALA['name'], numOfThrows2),
            check_throw(mockThrow3, GENERALA['name'], numOfThrows3),
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
            check_throw(mockThrow, GENERALA['name'], numOfThrows),
            check_throw(mockThrow2, GENERALA['name'], numOfThrows2),
            check_throw(mockThrow3, GENERALA['name'], numOfThrows3),
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
            check_throw(mockThrow, GENERALA['name'], numOfThrows),
            check_throw(mockThrow2, GENERALA['name'], numOfThrows2),
            check_throw(mockThrow3, GENERALA['name'], numOfThrows3),
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
            check_throw(mockThrow, GENERALA['name'], numOfThrows),
            check_throw(mockThrow2, GENERALA['name'], numOfThrows2),
            check_throw(mockThrow3, GENERALA['name'], numOfThrows3),
        ]
        self.assertTrue(isGeneralaDoble[0])
        self.assertTrue(isGeneralaDoble[1])
        self.assertTrue(isGeneralaDoble[2])

    def test_number_one(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 4, 4]
        sumOfOnes = check_throw(mockThrow, UNO['name'], numOfThrows)
        self.assertEqual(sumOfOnes, 3)

    def test_not_number_one(self):
        numOfThrows = 1
        mockThrow2 = [5, 6, 3, 4, 2]
        sumOfOnes2 = check_throw(mockThrow2, UNO['name'], numOfThrows)
        self.assertEqual(sumOfOnes2, 0)

    def test_number_two(self):
        numOfThrows = 1
        mockThrow = [2, 2, 2, 4, 4]
        sumOfTwos = check_throw(mockThrow, DOS['name'], numOfThrows)
        self.assertEqual(sumOfTwos, 6)

    def test_not_number_two(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 1, 4]
        sumOfTwos2 = check_throw(mockThrow2, DOS['name'], numOfThrows)
        self.assertEqual(sumOfTwos2, 0)

    def test_number_three(self):
        numOfThrows = 1
        mockThrow = [3, 3, 3, 4, 2]
        sumOfThrees = check_throw(mockThrow, TRES['name'], numOfThrows)
        self.assertEqual(sumOfThrees, 9)

    def test_not_number_three(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 1, 4, 2]
        sumOfThrees2 = check_throw(mockThrow2, TRES['name'], numOfThrows)
        self.assertEqual(sumOfThrees2, 0)

    def test_number_four(self):
        numOfThrows = 1
        mockThrow = [1, 1, 1, 4, 4]
        sumOfFours = check_throw(mockThrow, CUATRO['name'], numOfThrows)
        self.assertEqual(sumOfFours, 8)

    def test_not_number_four(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 1, 2]
        sumOfFours2 = check_throw(mockThrow2, CUATRO['name'], numOfThrows)
        self.assertEqual(sumOfFours2, 0)

    def test_number_five(self):
        numOfThrows = 1
        mockThrow = [1, 5, 5, 4, 4]
        sumOfFives = check_throw(mockThrow, CINCO['name'], numOfThrows)
        self.assertEqual(sumOfFives, 10)

    def test_not_number_five(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 3, 4, 2]
        sumOfFives2 = check_throw(mockThrow2, CINCO['name'], numOfThrows)
        self.assertEqual(sumOfFives2, 0)

    def test_number_six(self):
        numOfThrows = 1
        mockThrow = [1, 6, 6, 4, 4]
        sumOfSixes = check_throw(mockThrow, SEIS['name'], numOfThrows)
        self.assertEqual(sumOfSixes, 12)

    def test_not_number_six(self):
        numOfThrows = 1
        mockThrow2 = [1, 1, 5, 4, 2]
        sumOfSixes2 = check_throw(mockThrow2, SEIS['name'], numOfThrows)
        self.assertEqual(sumOfSixes2, 0)
