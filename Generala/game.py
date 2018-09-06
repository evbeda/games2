from .player import Player
from .throw import Throw
from .utils import check_throw


class Game():
    name = 'Generala'
    input_args = 2

    def __init__(self, name='Santi', name2='Beto'):
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.turno = self.player1
        self.dados = []
        self.dados_desordenados = []
        self.is_playing = True
        self.round = 1
        self.which_to_roll = [0, 1, 2, 3, 4, ]
        self.throw = Throw()

    def finished(self):
        if self.player1.score >= 3000:
            return True

        if self.player2.score >= 3000:
            return True

        for key, value in self.player1.combinations.items():
            if self.player1.combinations[key] == '':
                return False
        for key, value in self.player2.combinations.items():
            if self.player2.combinations[key] == '':
                return False
        return True

    def next_turn(self):
        if self.throw.is_possible_to_roll():
            # import ipdb; ipdb.set_trace()
            # self.throw.roll(self.which_to_roll)
            return '{}\nTu tirada: {} \nIngrese CONSERVAR X, ANOTAR CATEGORIA\
 o TIRAR YA\nx'.format(
                self.turno.name,
                str(self.throw.dice),
            )
        else:
            return (
                '{}\nTu tirada: {} \nElija la categoria\n\
                 que desea llenar (Ej: POKER, GENERALA, ETC.)'.format(
                    self.turno.name,
                    self.throw.dice,
                )
            )

    def play(self, text_input, value):
        if 'CONSERVAR' == text_input:
            dados_a_conservar = value.split(',')
            # import ipdb; ipdb.set_trace()
            self.which_to_roll = [0, 1, 2, 3, 4, ]
            for dado_index in dados_a_conservar:
                dice_to_check = int(dado_index)
                if dice_to_check in self.which_to_roll:
                    self.which_to_roll.remove(dice_to_check)
            self.throw.roll(self.which_to_roll)

        elif 'TIRAR' == text_input:
            self.next_turn()
            self.throw.roll([0, 1, 2, 3, 4, ])
        elif 'ANOTAR' == text_input:
            categoria = value
            your_dices = self.throw.dice
            # print('DADOS {}'.format(your_dices))
            # print('CATEGORIA {}'.format(categoria))
            # print('TURNO {}'.format(self.throw.number))
            points = check_throw(your_dices, categoria, self.throw.number)
            is_possible = self.turno.choose_combination(categoria, points)
            if is_possible:
                self.cambiar_turno()
                self.is_playing = not self.finished()
                return 'ANOTADO EN: {} - PUNTAJE: {}'.format(
                    categoria,
                    str(points),
                )
            else:
                return 'Categoria ya asignada'
        else:
            return 'Ingrese ANOTAR (TIRADA), CONSERVAR (1,2..), o TIRAR'

    # @property
    def board(self):
        return '{} TIENE {} PUNTOS \n{} TIENE {} PUNTOS\nRONDA {}'.format(
            self.player1.name,
            self.player1.score,
            self.player2.name,
            self.player2.score,
            self.round,
        )

    def cambiar_turno(self):
        self.dados = []
        self.throw = Throw()
        self.turno.tirada = 1
        if self.turno == self.player1:
            self.turno = self.player2
        else:
            self.turno = self.player1
        self.round += 1

    # def tirar(self, indexes):
    #     self.dados_desordenados = []
    #     for i in range(5 - len(self.dados)):
    #         self.dados_desordenados.append(random.randint(1, 6))
