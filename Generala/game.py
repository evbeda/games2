from .player import Player
from .utils import check_throw
import random


class Game():

    def __init__(self, name, name2):
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.turno = self.player1
        self.dados = []

    def finished(self):
        for key, value in self.player1.combinations.items():
            if self.player1.combinations[key] == '':
                return False
        for key, value in self.player2.combinations.items():
            if self.player2.combinations[key] == '':
                return False
        return True

    def next_turn(self):
        if self.turno.tirada != 4:
            self.tirar()
            self.turno.tirada += 1
            return (self.turno.name + ' Tu tirada: ' + str(self.dados) + ' INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA')
        else:
            return 'Eliga la categoria que desea llenar (NOMBRETIRADA)'

    def play(self, text_input):
        if 'CONSERVAR' in text_input:
            text_input = text_input.replace('CONSERVAR ', '')
            dados_a_conservar = text_input.split(', ')
            self.dados = []
            for dado in dados_a_conservar:
                self.dados.append(int(dado))
        elif 'ANOTAR' in text_input:
            self.turno.tirada = 4
            categoria = text_input.replace('ANOTAR ', '')
            points = check_throw(self.dados, categoria, self.turno.tirada)
            is_possible = self.turno.choose_combination(categoria, points)
            if is_possible:
                self.cambiar_turno()
                return 'ANOTADO EN: ' + categoria + ' PUNTAJE: ' + str(points)
            else:
                return 'Categoria ya asignada'

    # @property
    # def board(self, dados):
    #     return str(self.played_numbers)

    def cambiar_turno(self):
        self.turno.tirada = 1
        if self.turno == self.player1:
            self.turno = self.player2
        else:
            self.turno == self.player1

    def tirar(self):
        dados_desordenados = []
        for i in range(5 - len(self.dados)):
            dados_desordenados.append(random.randint(1, 6))
        self.dados += dados_desordenados
