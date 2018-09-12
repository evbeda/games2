import random

from truco.hand import Hand
from truco.player import (
    HumanPlayer,
    CPUPlayer,
)
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
            mensaje = (
                '0: Para jugar la primer carta \n'
                '1: Para jugar la segunda carta \n'
                '2: Para jugar la tercer carta \n'
                'MAZO: Ir al mazo \n'
            )
            if len(self.hand.envidos) == 0 and len(self.hand.trucos) == 0:
                mensaje += 'ENVIDO, REAL ENVIDO, FALTA ENVIDO: Para cantar envido \n'
            if len(self.hand.trucos) == 0:
                mensaje += 'TRUCO: Para cantar Truco \n'
            return mensaje
        else:
            return '\nGame Over!'

    def play(self, command):
        if (command == "ENVIDO" or
                command == "REAL ENVIDO" or
                command == "FALTA ENVIDO"):
            return self.envido_logic(command)
        if command == "TRUCO" and self.hand.truco_fase:
            return self.truco_logic(command)
        if command == 'ACCEPTED':
            if self.hand.truco_pending is True:
                self.hand.truco_pending = False
            self.hand.envido_fase = False
        if command.isdigit():
            self.hand.play_card(int(command))
            self.cpu_auto_play()
            self.hand.siguiente_ronda()
            self.hand.who_is_next()
        else:
            return "\nComando Erroneo"
        if not self.hand.is_playing:
            return self.hand_finish_logic()
        return "\nSiguiente ronda"

    def truco_logic(self, command):
        try:
            self.hand.sing_truco(command)
            result = self.players[1].ask_trucos(self.hand.trucos)
            if result == 'ACCEPTED':
                self.hand.accept_truco()
            elif result == 'REJECTED':
                self.hand.reject_truco()
            else:
                self.hand.accept_truco()
                self.hand.sing_truco(result)
        except Exception:
            return "No en fase de truco"
        return result

    def hand_finish_logic(self):
        self.players[self.hand.winner_index].score += self.hand.get_truco_points()
        if self.players[0].score > 14 or self.players[1].score > 14:
            self.is_playing = False
            return "\nFin del juego"
        self.hand = Hand()
        self.hand.mano = 1 if self.hand.mano is 0 else 0
        return "\nLa mano termino\n{}{}".format(self.hand.show_cards(), "-----------")

    def cpu_auto_play(self):
        result = self.players[1].cpu_play()
        if result == 'ENVIDO':
            self.hand.envidos.append(random.choice(envido_posibilities))
            self.hand.play_card(random.randint(
                0, len(self.hand.hidden_cards[1]) - 1))
        elif result == 'JUGAR':
            self.hand.play_card(random.randint(
                0, len(self.hand.hidden_cards[1]) - 1))

    def envido_logic(self, command):
        try:
            self.hand.sing_envido(command)
            result = self.players[1].ask_envido(self.hand.envidos)  # CPU
            if result == 'ACCEPTED':
                self.hand.accept_envido()
                # Problems with who_is_next.
                # Look the "play" method in command.isdigit
                self.players[self.hand.get_envido_winner(
                )].score += self.hand.get_envido_points()
            elif result == 'REJECTED':
                self.hand.reject_envido()
            else:
                self.hand.sing_envido(result)
        except Exception:
            return "No en fase de envido"

        mensaje = "\nLos puntos del envido fueron \nHumano : {} \nPC: {}"
        return mensaje.format(
            self.players[0].score,
            self.players[1].score,
        )

    def show_scores(self):
        mensaje = "\nPuntajes:\nHumano:{} \nPC:{}"
        return mensaje.format(self.players[0].score, self.players[1].score)
