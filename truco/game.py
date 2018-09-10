from truco.hand import Hand
from truco.player import (
    HumanPlayer,
    CPUPlayer,
)
import random
from .hand import envido_posibilities


class Game(object):
    name = 'Truco Game'
    input_args = 1

    def __init__(self):
        self.players = [HumanPlayer('P1'), CPUPlayer('P2')]
        self.cantos_envidos = []
        self.is_playing = True
        self.hand = Hand()

    @property
    def board(self):
        return self.hand.show_cards() + self.show_scores()

    def next_turn(self):
        if self.is_playing is True:
            return '\nE: Para cantar envido \nT: Para cantar Truco \n0: Para jugar la primer carta \n1: Para jugar la segunda carta\n2: Para jugar la tercer carta'
        else:
            return '\nGame Over!'

    def play(self, command):
        if (command == "ENVIDO" or
            command == "REAL ENVIDO" or
                command == "FALTA ENVIDO"):
            return self.envido_logic(command)
        if command == "TRUCO" and self.hand.truco_fase:
            return self.truco_logic()
        if command == 'ACCEPTED':
            self.hand.envido_fase = False
        if command.isdigit():
            self.normal_round_logic(command)
            self.cpu_auto_play()

        else:
            return "\nComando Erroneo"
        if not self.hand.is_playing:
            return self.hand_finish_logic()
        return "\nSiguiente ronda"

    def truco_logic(self):
        self.hand.truco_fase = False
        return "\nTruco cantado, al final de la mano se suman los puntos"

    def hand_finish_logic(self):
        self.players[self.hand.winner_index].score += 1
        if not self.hand.truco_fase:
            self.players[self.hand.winner_index].score += 1
        if self.players[0].score > 14 or self.players[1].score > 14:
            self.is_playing = False
            return "\nFin del juego"
        self.hand = Hand()
        self.hand.mano = 1 if self.hand.mano is 0 else 0
        return "\nLa mano termino\n{}{}".format(self.hand.show_cards(), "-----------")

    def normal_round_logic(self, command):
        self.hand.play_card(int(command))
        self.hand.play_card(int(command))  # PC
        self.hand.siguiente_ronda()
        self.hand.who_is_next()

    def cpu_auto_play(self):
        result = self.players[1].cpu_play()
        if result == 'ENVIDO':
            self.hand.envidos.append(random.choice(envido_posibilities))
        elif result == 'JUGAR':
            self.hand.play_card(random.randint(
                0, len(self.hand.hidden_cards[1])))

    def envido_logic(self, command):
        try:
            self.hand.sing_envido(command)
            result = self.players[1].ask_envido(self.hand.envidos)
            if result == 'ACCEPTED':
                self.hand.accept_envido()
            elif result == 'REJECTED':
                self.hand.reject_envido()
            else:
                self.hand.sing_envido(result)
        except Exception:
            return "No en fase de envido"
        human_points = self.hand.get_score_envido(0)
        pc_points = self.hand.get_score_envido(1)
        i = 0 if human_points > pc_points else 1
        self.players[i].score += 2
        mensaje = "\nLos puntos del envido fueron \nHumano : {} \nPC: {}"
        return mensaje.format(human_points, pc_points)

    def show_scores(self):
        mensaje = "\nPuntajes:\nHumano:{} \nPC:{}"
        return mensaje.format(self.players[0].score, self.players[1].score)
