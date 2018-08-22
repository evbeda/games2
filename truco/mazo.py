import random
from .carta import Carta
from . import ESPADA, BASTO, ORO, COPA


class Mazo():

	def __init__(self):
		self.mazo = [
			Carta(ESPADA, 1), Carta(BASTO, 1), Carta(ESPADA, 7),
			Carta(ORO, 7),Carta(ESPADA, 3),Carta(BASTO, 3),Carta(ORO, 3),Carta(COPA, 3),
			Carta(ESPADA, 2),Carta(BASTO, 2),Carta(ORO, 2),Carta(COPA, 2),
			Carta(ORO, 1),Carta(COPA, 1),
			Carta(ESPADA, 12),Carta(BASTO, 12),Carta(ORO, 12),Carta(COPA, 12),
			Carta(ESPADA, 11),Carta(BASTO, 11),Carta(ORO, 11),Carta(COPA, 11),
			Carta(ESPADA, 10),Carta(BASTO, 10),Carta(ORO, 10),Carta(COPA, 10),
			Carta(BASTO, 7),Carta(COPA, 7),
			Carta(ESPADA, 6),Carta(BASTO, 6),Carta(ORO, 6),Carta(COPA, 6),
			Carta(ESPADA, 5),Carta(BASTO, 5),Carta(ORO, 5),Carta(COPA, 5),
			Carta(ESPADA, 4),Carta(BASTO, 4),Carta(ORO, 4),Carta(COPA, 4)]
	def obtenerCarta(self):
		indice = random.randint(0,len(self.mazo)-1)
		aux = self.mazo[indice]
		del self.mazo[indice]
		return aux