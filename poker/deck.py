from .card import Card
from random import shuffle


class Deck(object):
    def __init__(self):
        self.rebuild()

    def create(self):
        colors = ['h', 'd', 's', 'c']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        return [Card(value, color) for value in values for color in colors]

    def shuffle_cards(self):
        shuffle(self.cards)

    def deal(self, number):
        result = []
        for card in range(number):
            result.append(self.cards[0])
            self.cards.pop()
        return result

    def rebuild(self):
        self.cards = self.create()
        self.shuffle_cards()
