from truco.hand import Hand
from truco.player import Player


class Game(object):
    name = 'Truco Game'
    input_args = 1

    def __init__(self):
        self.players = [Player('P1'), Player('P2')]
        self.cantos_envidos = []
        self.is_playing = True
        self.hand = Hand()

    @property
    def board(self):
        if not self.hand.is_playing:
            self.hand = Hand()
            self.hand.mano = 1 if self.hand.mano is 0 else 0
        return self.hand.show_cards() + self.show_scores()

    def next_turn(self):
        if self.is_playing is True:
            return '\nE: Para cantar envido \nT: Para cantar Truco \n0: Para jugar la primer carta \n1: Para jugar la segunda carta\n2: Para jugar la tercer carta'
        else:
            return '\nGame Over!'

    def play(self, command):
        if command is "E" and self.hand.envido_fase is True:
            return self.envido_logic()
        if command is "T" and self.hand.truco_fase is True:
            return self.truco_logic()
        if command.isdigit():
            self.normal_round_logic(command)
        else:
            return "\nComando Erroneo"
        if self.hand.is_playing is False:
            return self.hand_finish_logic()
        return "\nSiguiente ronda"

    def truco_logic(self):
        self.hand.truco_fase = False
        return "\nTruco cantado, al final de la mano se suman los puntos"

    def hand_finish_logic(self):
        self.players[self.hand.winner_index].score += 1
        if self.hand.truco_fase is False:
            self.players[self.hand.winner_index].score += 1
        if self.players[0].score > 14 or self.players[1].score > 14:
            self.is_playing = False
            return "\nFin del juego"
        return "\nLa mano termino\n{}{}".format(self.hand.show_cards(), "-----------")

    def normal_round_logic(self, command):
        self.hand.play_card(int(command))
        self.hand.play_card(int(command))  # PC
        self.hand.siguiente_ronda()
        self.hand.who_is_next()

    def envido_logic(self):
        self.hand.envido_fase = False
        human_points = self.hand.get_score_envido(0)
        pc_points = self.hand.get_score_envido(1)
        i = 0 if human_points > pc_points else 1
        self.players[i].score += 2
        mensaje = "\nLos puntos del envido fueron \nHumano : {} \nPC: {}"
        return mensaje.format(human_points, pc_points)

    def show_scores(self):
        mensaje = "\nPuntajes:\nHumano:{} \nPC:{}"
        return mensaje.format(self.players[0].score, self.players[1].score)
