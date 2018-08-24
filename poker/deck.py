from .card import Card
from random import shuffle


class Deck(object):
    def __init__(self):
        self.cards = self.create()
        self.shuffle_cards(self.cards)

    def create(self):
        colors = ['h', 'd', 's', 'c']
        return [Card(value, color) for value in range(1, 14) for color in colors]

    def shuffle_cards(self, cards):
        shuffle(cards)
