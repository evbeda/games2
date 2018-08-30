from .deck import Deck
from .poker import PREFLOP, FLOP, TURN, RIVER


class Hand():
    def __init__(self):
        self.pot = 0
        self.deck = Deck()
        self.stage = 0
        self.player01_cards = self.deck.deal(2)
        self.player02_cards = self.deck.deal(2)
        self.common_cards = []

    def deal_cards(self):
        if self.stage == FLOP:
            self.common_cards = self.deck.deal(3)
        elif self.stage == TURN or self.stage == RIVER:
            self.common_cards.append(self.deck.deal(1)[0])

    def next_stage(self):
        if(self.stage < 4):
            self.stage += 1
    
    
