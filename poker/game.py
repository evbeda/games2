from .player import Player
from .hand import Hand
from .poker import (
    CHECK,
    CALL,
    BET,
    FOLD,
    RAISE,
)


class PokerGame(object):
    def __init__(self):
        self.player = Player(100)
        self.cpu = Player(100)
        self.is_playing = True
        self.hand = Hand([self.player, self.cpu])

    def next_turn(self):
        if self.player_no_money():
            return self.player_no_money()
        if self.is_playing:
            if self.hand.turn == 'player':
                if self.hand.stage < 5:
                    actions = self.hand.possibles_actions()
                    return_string = ''
                    for action in actions:
                        return_string += ' ' + action + '({})'.format(action[:2])
                        if action == BET or action == RAISE:
                            return_string += ' your bet'
                        return_string += '\n'
                    return return_string
                else:
                    return 'Show Down!'

    def play(self, command):
        pass

    def player_no_money(self):
        if self.player.money == 0:
            return 'Player loses'
        elif self.cpu.money == 0:
            return 'CPU loses'
        return False
