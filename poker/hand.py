from .deck import Deck
from .poker import PREFLOP, FLOP, TURN, RIVER
from .poker import CHECK, CALL, BET, RAISE, FOLD
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
)


class Hand():
    def __init__(self):
        self.pot = 0
        self.deck = Deck()
        self.stage = 0
        self.player01_cards = self.deck.deal(2)
        self.player02_cards = self.deck.deal(2)
        self.common_cards = []
        self.bet_time = True
        self.last_bet = CHECK

    def deal_cards(self):
        if self.stage == FLOP:
            self.common_cards = self.deck.deal(3)
        elif self.stage == TURN or self.stage == RIVER:
            self.common_cards.append(self.deck.deal(1)[0])

    def next_stage(self):
        if(self.stage < 4):
            self.stage += 1
            self.deal_cards()
        else:
            a = transform_cards_to_str(self.player01_cards) + transform_cards_to_str(self.common_cards)
            b = transform_cards_to_str(self.player02_cards) + transform_cards_to_str(self.common_cards)
            return [better_hand(combine_card(a)), better_hand(combine_card(b))]
