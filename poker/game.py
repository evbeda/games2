from .player import Player
from .hand import Hand
from .poker import (
    CHECK,
    CALL,
    BET,
    FOLD,
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
                    # actions = self.hand.possibles_actions() # TODO in Hand
                    actions = [BET, CHECK, FOLD]
                    return_string = ''
                    for action in actions:
                        return_string += ' ' + action + '({})'.format(action[:2])
                        if action == BET or action == RAISE:
                            return_string += 'your bet'
                        return_string += '\n'
                    return return_string
                else:
                    return 'Show Down!'

    # def play(self, command):


    def player_no_money(self):
        if self.player.money == 0:
            return 'Player loses'
        elif self.cpu.money == 0:
            return 'CPU loses'
        return False

    def take_bets(self, player1_bet, player2_bet):
        if self.player1.money >= player1_bet:
            self.pot += player1_bet
        else:
            # print("Not enough money")
            return False
            # deberia ir el metodo que llame a take bets desde la consola
        if self.player2.money >= player2_bet:
            self.pot += player2_bet
        else:
            # print("Not enough money")
            return False
            # deberia ir el metodo que llame a take bets desde la consola
        return True
