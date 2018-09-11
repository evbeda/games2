from .deck import Deck
from .poker import PREFLOP, FLOP, TURN, RIVER
from .poker import CHECK, CALL, BET, RAISE, FOLD, NONE
from .poker import (
    transform_cards_to_str,
    combine_card,
    better_hand,
    find_straight_flush,
    find_royal_flush,
    find_repeated_cards,
    find_flush,
    find_cards_suits,
    find_straight,
    sort_cards_by_number,
    get_value,
    PLAYER, CPU,
)


class Hand():
    def __init__(self, players, first = PLAYER):
        self.pot = 0
        self.deck = Deck()
        self.stage = 0
        self.player_cards = self.deck.deal(2)
        self.cpu_cards = self.deck.deal(2)
        self.common_cards = []
        self.first = first
        self.turn = first
        self.last_action = NONE
        self.last_bet = 0
        self.players = players


    def deal_cards(self):
        if self.stage == FLOP:
            self.common_cards = self.deck.deal(3)
        elif self.stage == TURN or self.stage == RIVER:
            self.common_cards.append(self.deck.deal(1)[0])

    def next_stage(self):
        if(self.stage < 4):
            self.stage += 1
            self.deal_cards()
            self.last_action = NONE
            self.last_bet = 0
        else:
            a = transform_cards_to_str(self.player_cards) + transform_cards_to_str(self.common_cards)
            b = transform_cards_to_str(self.cpu_cards) + transform_cards_to_str(self.common_cards)
            player_game = better_hand(combine_card(a))
            cpu_game = better_hand(combine_card(b))
            return [player_game, cpu_game]

    def take_action(self, action, bet=0):
        if action == CHECK:
            if self.last_action == CHECK:
                self.next_stage()
            else:
                self.last_action = action
        if action == BET:
            if self.last_action == RAISE:
                return "You can't bet now"
            elif self.turn == PLAYER and self.players[0].money < bet:
                return "You don't have enough money"
            else:
                self.last_action = action
                self.pot += bet
                self.last_bet = bet
                if self.turn == PLAYER:
                    self.players[0].money -= bet
                else:
                    self.players[1].money -= bet
        if action == CALL:
            if self.last_action == BET or self.last_action == RAISE:
                if self.turn == PLAYER:
                    self.players[0].money -= self.last_bet
                elif self.turn == CPU:
                    self.players[1].money -= self.last_bet
                self.pot += self.last_bet
                self.next_stage()
            else:
                return "You can't CALL now"
        if action == FOLD:
            if self.last_action == BET or self.last_action == RAISE:
                if self.turn == CPU:
                    self.players[0].money += self.pot
                elif self.turn == PLAYER:
                    self.players[1].money += self.pot
                return "the {} win".format(PLAYER if (self.turn == CPU) else CPU)
            else:
                return "You can't FOLD now"
        if action == RAISE:
            if self.last_action == BET or self.last_action == RAISE:
                if self.turn == PLAYER and self.players[0].money < bet:
                    return "You don't have enough money"
                elif bet >= 2 * self.last_bet:
                    self.last_action = action
                    self.pot += bet
                    self.last_bet = bet - self.last_bet
                    if self.turn == PLAYER:
                        self.players[0].money -= bet
                    else:
                        self.players[1].money -= bet
                else:
                    return "You must raise at least twice last bet"
        self.turn = PLAYER if (self.turn == CPU) else CPU

    def possibles_actions(self):
        if self.last_action == NONE or self.last_action == CHECK:
            return [CHECK, BET]
        if self.last_action == BET or self.last_action == RAISE:
            return [CALL, RAISE, FOLD]
        