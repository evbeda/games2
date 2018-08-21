import unittest
from check_throw import checkThrow

class test_categories(unittest.TestCase):

	def test_generala(self):
		numOfThrows = 2
		mockThrow = [1,1,1,1,1]
		isGenerala = checkThrow(mockThrow, "generala", numOfThrows)		
		self.assertTrue(isGenerala)

	def test_not_generala(self):
		numOfThrows = 2
		mockThrow = [2,3,1,1,1]
		isNotGenerala = checkThrow(mockThrow, "generala", numOfThrows)
		self.assertFalse(isNotGenerala)

	def test_not_generala_is_servida(self):
		numOfThrows = 1
		mockThrow = [1,1,1,1,1]
		isNotGenerala = checkThrow(mockThrow, "generala", numOfThrows)
		self.assertFalse(isNotGenerala)

	def test_poker(self):
		numOfThrows = 1
		mockThrow = [1,5,1,1,1]
		isPoker = checkThrow(mockThrow, "poker", numOfThrows)
		self.assertTrue(isPoker)

	def test_not_poker(self):
		numOfThrows = 1
		mockThrow = [3,3,3,1,1]
		isNotPoker = checkThrow(mockThrow, "poker", numOfThrows)
		self.assertFalse(isNotPoker)

	def test_full(self):
		numOfThrows = 1
		mockThrow = [1,1,1,5,5]
		isFull = checkThrow(mockThrow, "full", numOfThrows)
		self.assertTrue(isFull)

	def test_not_full(self):
		numOfThrows = 1
		mockThrow = [3,3,4,1,1]
		isNotFull = checkThrow(mockThrow, "full", numOfThrows)
		self.assertFalse(isNotFull)

	def test_escalera(self):
		numOfThrows = 1
		mockThrow = [2,3,4,5,6]
		isEscalera = checkThrow(mockThrow, "escalera", numOfThrows)
		self.assertTrue(isEscalera)

	def test_not_escalera(self):
		numOfThrows = 1
		mockThrow = [1,2,4,5,6]
		isNotEscalera = checkThrow(mockThrow, "escalera", numOfThrows)
		self.assertFalse(isNotEscalera)

	# def test_generala_servida(self):
	# 	numOfThrows = 1
	# 	mockThrow = [1,1,1,1,1]
	# 	isGeneralaServida = checkThrow(mockThrow, "generalaServida", numOfThrows)
	# 	self.assertTrue(isGeneralaServida)

	# def test_not_generala_servida(self):
	# 	numOfThrows = 2
	# 	mockThrow = [1,1,1,1,1]
	# 	isNotGeneralaServida = checkThrow(mockThrow, "generalaServida", numOfThrows)
	# 	self.assertFalse(isNotGeneralaServida)

	# def test_generala_doble(self):
	# 	numOfThrows = 1
	# 	numOfThrows2 = 2
	# 	numOfThrows3 = 3
	# 	mockThrow = [1,3,4,3,4]
	# 	mockThrow2 = [2,2,2,2,2]
	# 	mockThrow3 = [4,4,4,4,4]
	# 	isGeneralaDoble = [checkThrow(mockThrow, "generala", numOfThrows), checkThrow(mockThrow2, "generala", numOfThrows2), checkThrow(mockThrow3, "generala", numOfThrows3)]
	# 	self.assertFalse(isGeneralaDoble[0])
	# 	self.assertTrue(isGeneralaDoble[1])
	# 	self.assertTrue(isGeneralaDoble[2])

	# def test_not_generala_doble(self):
	# 	numOfThrows = 1
	# 	numOfThrows2 = 2
	# 	numOfThrows3 = 3
	# 	mockThrow = [1,3,4,3,4]
	# 	mockThrow3 = [4,4,4,4,4]
	# 	mockThrow4 = [3,2,2,2,1]
	# 	isNotGeneralaDoble = [checkThrow(mockThrow, "generala", numOfThrows), checkThrow(mockThrow4, "generala", numOfThrows2), checkThrow(mockThrow3, "generala", numOfThrows3)]
	# 	self.assertFalse(isNotGeneralaDoble[0])
	# 	self.assertFalse(isNotGeneralaDoble[1])
	# 	self.assertTrue(isNotGeneralaDoble[2])

	# def test_number_one(self):
	# 	numOfThrows = 1
	# 	mockThrow = [1,1,1,4,4]
	# 	sumOfOnes = checkThrow(mockThrow, 3, numOfThrows)
	# 	self.assertTrue(sumOfOnes)

	# def test_not_number_one(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,3,4,2]
	# 	sumOfOnes2 = checkThrow(mockThrow2, 3, numOfThrows)
	# 	self.assertFalse(sumOfOnes2)

	# def test_number_two(self):
	# 	numOfThrows = 1
	# 	mockThrow = [2,2,2,4,4]
	# 	sumOfTwos = checkThrow(mockThrow, 6, numOfThrows)
	# 	self.assertTrue(sumOfOnes)

	# def test_not_number_two(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,3,2,2]
	# 	sumOfTwos2 = checkThrow(mockThrow2, 6, numOfThrows)
	# 	self.assertFalse(sumOfTwos2)

	# def test_number_three(self):
	# 	numOfThrows = 1
	# 	mockThrow = [3,3,3,4,4]
	# 	sumOfThrees = checkThrow(mockThrow, 9, numOfThrows)
	# 	self.assertTrue(sumOfThrees)

	# def test_not_number_three(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,3,4,2]
	# 	sumOfThrees2 = checkThrow(mockThrow2, 9, numOfThrows)
	# 	self.assertFalse(sumOfThrees2)

	# def test_number_four(self):
	# 	numOfThrows = 1
	# 	mockThrow = [1,1,1,4,4]
	# 	sumOfFours = checkThrow(mockThrow, 8, numOfThrows)
	# 	self.assertTrue(sumOfFours)

	# def test_not_number_four(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,3,4,2]
	# 	sumOfFours2 = checkThrow(mockThrow2, 8, numOfThrows)
	# 	self.assertFalse(sumOfFours2)

	# def test_number_five(self):
	# 	numOfThrows = 1
	# 	mockThrow = [1,5,5,4,4]
	# 	sumOfFives = checkThrow(mockThrow, 10, numOfThrows)
	# 	self.assertTrue(sumOfFives)

	# def test_not_number_five(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,5,4,2]
	# 	sumOfFives2 = checkThrow(mockThrow2, 10, numOfThrows)
	# 	self.assertFalse(sumOfFives2)

	# def test_number_six(self):
	# 	numOfThrows = 1
	# 	mockThrow = [1,6,6,4,4]
	# 	sumOfSixes = checkThrow(mockThrow, 12, numOfThrows)
	# 	self.assertTrue(sumOfSixes)

	# def test_not_number_six(self):
	# 	numOfThrows = 1
	# 	mockThrow2 = [1,1,6,4,2]
	# 	sumOfSixes2 = checkThrow(mockThrow2, 12, numOfThrows)
	# 	self.assertFalse(sumOfSixes2)

if __name__=='__main__':
	unittest.main()