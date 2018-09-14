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
        if self.hand.mazo is True:
            self.hand = Hand()
        return self.hand.show_cards() + self.show_scores()

    def next_turn(self):
        mensaje = ""
        if self.hand.envido_solved is False or self.hand.truco_pending:
            return ('ACCEPTED: To accept\n'
                    'REJECTED: To reject\n')
        if self.is_playing is True:
            for index in range(len(self.hand.hidden_cards[0])):
                mensaje += '{} to play {}\n'.format(
                    index, self.hand.hidden_cards[0][index])
            if self.hand.envido_fase:
                mensaje += 'ENVIDO, REAL_ENVIDO, FALTA_ENVIDO: Sing envido \n'
            mensaje += 'DECK: Go to the Deck \n'
            if len(self.hand.trucos) == 0:
                mensaje += 'TRUCO: Sing truco \n'
            return mensaje
        else:
            return '\nGame Over!'

    def play(self, command):
        if self.hand.envido_solved is False and command in self.hand.get_response_envido() or self.hand.envido_solved:
            if (
                    self.hand.truco_pending and
                    command in self.hand.get_response_truco() or
                    self.hand.truco_pending is False
            ):
                if command in envido_posibilities:
                    return self.envido_logic(command)
                if command == "TRUCO" and self.hand.truco_fase:
                    return self.truco_logic(command)
                if command == "ACCEPTED":
                    return self.accept()
                if command == "REJECTED":
                    return self.reject()
                if command.isdigit():
                    return self.digit_logic(command)
                if command == "DECK":
                    self.hand.mazo = True
                    if self.hand.number_hand == 1:
                        points = 2
                    else:
                        points = 1
                    self.players[1].score += points
                    return "You go to the deck. You lose {} points.".format(points)
                else:
                    return "\nWrong input"
            else:
                return "\nYou must accept or reject the truco"
        else:
            return "\nYou must accept or reject the envido"

    def cheque_if_cpu_must_play(self):
        if len(self.hand.played_cards[0]) > len(self.hand.played_cards[1]):
            self.hand.play_card(random.randint(
                0, len(self.hand.hidden_cards[1]) - 1))

    def digit_logic(self, command):
        self.hand.play_card(int(command))
        move, especific = self.cpu_auto_play()
        if move == "ENVIDO" or move == "TRUCO":
            return "The machine said {}".format(especific)
        else:
            self.hand.siguiente_ronda()
            self.hand.who_is_next()
            if not self.hand.is_playing:
                return self.hand_finish_logic()
            return "The machine play {}".format(especific)

    def reject(self):
        if self.hand.truco_pending is True:
            self.hand.reject_truco()
            self.players[1].score += self.hand.get_truco_points(1)
            self.cheque_if_cpu_must_play()
            return "You reject truco. You lose {} points".format(self.hand.get_truco_points(1))
        else:
            puntos = self.envido_points(1)
            self.players[1].score += puntos
            self.hand.reject_envido()
            self.cheque_if_cpu_must_play()
            return "You reject envido. You lose {} points".format(puntos)

    def accept(self):
        if self.hand.truco_pending is True:
            self.hand.accept_truco()
            self.cheque_if_cpu_must_play()
            return "The truco will be evaluated at the end of the game"
        else:
            self.hand.accept_envido()
            self.players[self.hand.get_envido_winner(
            )].score += self.envido_points()
            self.cheque_if_cpu_must_play()
            return "Won the player: {}".format(self.hand.get_envido_winner())

    def truco_logic(self, command):
        try:
            self.hand.sing_truco(command)
            result = self.players[1].ask_trucos(self.hand.trucos)
            if result == 'ACCEPTED':
                self.hand.accept_truco()
                return result
            elif result == 'REJECTED':
                self.hand.reject_truco()
                self.players[0].score += self.hand.get_truco_points(1)
                return "The machine reject the Truco. You won {} points".format(self.hand.get_truco_points(1))
            else:
                self.hand.accept_truco()
                self.hand.sing_truco(result)
                return "The machine said {}".format(result)
        except Exception:
            return "Not in fase truco"

    def hand_finish_logic(self):
        self.players[self.hand.winner_index].score += self.hand.get_truco_points()
        if self.players[0].score > 14 or self.players[1].score > 14:
            self.is_playing = False
            return "\nGame Over."
        messaje = "\nThe hand is over\n{}{}".format(self.hand.show_cards(), "-----------")
        self.hand = Hand()
        self.hand.mano = 1 if self.hand.mano is 0 else 0
        return messaje

    def get_what_machine_can_do(self):
        possibles = ['PLAY']
        if self.hand.envido_fase is True:
            possibles.append('ENVIDO')
        if len(self.hand.trucos) == 0:
            possibles.append('TRUCO')
        return possibles

    def cpu_auto_play(self):
        especific = ""
        move = self.players[1].cpu_play(self.get_what_machine_can_do())
        if move == 'ENVIDO':
            self.hand.envidos.append(random.choice(envido_posibilities))
            especific = self.hand.envidos[-1]
        elif move == 'PLAY':
            self.hand.play_card(random.randrange(len(self.hand.hidden_cards[1])))
            especific = self.hand.played_cards[1][-1]
        elif move == 'TRUCO':
            self.hand.sing_truco('TRUCO')
            especific = self.hand.trucos[-1]
        return move, especific

    def envido_points(self, won=0):
        points = self.hand.get_envido_points(won=won)
        if points == 99:
            winner = self.hand.get_envido_winner()
            if winner == 1:
                looser = 0
            else:
                looser = 1
            return 30 - self.players[looser].score
        else:
            return points

    def envido_logic(self, command):
        try:
            self.hand.sing_envido(command)
            result = self.players[1].ask_envido(self.hand.envidos)  # CPU
            if result == 'ACCEPTED':
                self.hand.accept_envido()
                self.players[self.hand.get_envido_winner(
                )].score += self.envido_points()
                self.cheque_if_cpu_must_play()
                return ("Envido Accepted:"
                        "Won the player: {}".format(self.hand.get_envido_winner()))
            elif result == 'REJECTED':
                puntos = self.envido_points(1)
                self.players[0].score += puntos
                self.hand.reject_envido()
                self.cheque_if_cpu_must_play()
                return "The machine reject the Envido. You won {} points".format(puntos)
            else:
                self.hand.sing_envido(result)
                return "The machine said {}".format(result)
        except Exception:
            return "Not in fase envido"

    def show_scores(self):
        mensaje = "\nPoints:\nHuman:{} \nComputer:{}"
        return mensaje.format(self.players[0].score, self.players[1].score)
