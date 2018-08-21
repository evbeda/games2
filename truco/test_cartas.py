import unittest
from carta import Carta
from __init__ import ESPADA, BASTO, ORO, COPA

class TestCartas (unittest.TestCase):
	#CREACIONES
	def test_si_se_crea_carta(self):
		carta1 = Carta(ESPADA,1)
		self.assertIsInstance(carta1,Carta)
	#POSICIONES
	def test_obtener_posicion_cero(self):
		cartaMacho = Carta(ESPADA,1)
		self.assertEqual(cartaMacho.obtenerPosicion(),0)
	def test_obtener_posicion_uno(self):
		cartaMacho = Carta(BASTO,1)
		self.assertEqual(cartaMacho.obtenerPosicion(),1)
	def test_obtener_posicion_trece(self):
		cartaMacho = Carta(ESPADA,4)
		self.assertEqual(cartaMacho.obtenerPosicion(),13)
	#COMPARACIONES
	def test_comparar_as_espadas_con_as_bastos(self):
	 	carta1 = Carta(ESPADA, 1)
		carta2 = Carta(BASTO, 1)
		result = carta1.esMasGrande(carta2)
		self.assertEqual(result,True)
	def test_comparar_4_de_espadas_con_4_de_bastos(self):
	 	carta1 = Carta(ESPADA, 4)
		carta2 = Carta(BASTO, 4)
		result = carta1.esMasGrande(carta2)
		self.assertEqual(result,0)
	def test_comparar_7_de_espadas_con_7_de_bastos(self):
	 	carta1 = Carta(ESPADA, 7)
		carta2 = Carta(BASTO, 7)
		result = carta1.esMasGrande(carta2)
		self.assertEqual(result,True)
	def test_comparar_5_de_espadas_con_2_de_bastos(self):
	 	carta1 = Carta(ESPADA, 5)
		carta2 = Carta(BASTO, 2)
		result = carta1.esMasGrande(carta2)
		self.assertEqual(result,False)
