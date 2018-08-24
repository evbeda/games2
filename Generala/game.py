from .player import Player
import random


class Game():

    def __init__(self, name, name2):
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.turno = self.player1
        self.dados = []

    def finished(self):
        if (
            len(self.player1.combinations) == 13 and
            len(self.player2.combinations) == 13
        ):
            return True
        else:
            return False

    def tirar(self):
        dados_desordenados = []
        for i in range(5 - len(self.dados)):
            dados_desordenados.append(random.randint(1, 6))
        for i in range(0, 5):
            while (True):
                result = (int(input('Seleccione un dado que quiera conservar (Escriba 0 para no seleccionar): ')))
                if result in dados_desordenados or result == 0:
                    break
                else:
                    print ('Ese numero no se encuentra disponible')
            if result == 0:
                break
            else:
                dados_desordenados.remove(result)
                self.dados.append(result)
