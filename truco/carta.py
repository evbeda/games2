from . import ESPADA, BASTO, ORO, COPA


class Carta():
	mazoJerarquico = (
		((ESPADA, 1,),),
		((BASTO, 1,),),
		((ESPADA, 7,),),
		((ORO, 7,),),
		((ESPADA, 3,),(BASTO, 3,),(ORO, 3,),(COPA, 3,),),
		((ESPADA, 2,),(BASTO, 2,),(ORO, 2,),(COPA, 2,),),
		((ORO, 1,),(COPA, 1,),),
		((ESPADA, 12,),(BASTO, 12,),(ORO, 12,),(COPA, 12,),),
		((ESPADA, 11,),(BASTO, 11,),(ORO, 11,),(COPA, 11,),),
		((ESPADA, 10,),(BASTO, 10,),(ORO, 10,),(COPA, 10,),),
		((BASTO, 7,),(COPA, 7,),),
		((ESPADA, 6,),(BASTO, 6,),(ORO, 6,),(COPA, 6,),),
		((ESPADA, 5,),(BASTO, 5,),(ORO, 5,),(COPA, 5,),),
		((ESPADA, 4,),(BASTO, 4,),(ORO, 4,),(COPA, 4,),),
		)
	def __init__(self,pinta,numero):
		self.pinta = pinta
		self.numero = numero
		self.posicion = self.obtenerPosicion()
	def obtenerPosicion(self):
		for i in range(len(self.mazoJerarquico)):
			for x in range(len(self.mazoJerarquico[i])):
				if self.pinta == self.mazoJerarquico[i][x][0] and self.numero == self.mazoJerarquico[i][x][1]:
					return i
	def esMasGrande(self, cartaDos):
		if self.posicion < cartaDos.posicion:
			return True
		elif self.posicion == cartaDos.posicion:
			return 0
		else:
			return False