import random


class Deck():
    def __init__(self, values, suits):
        self.values = values
        self.suits = suits
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(value + suit)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, amount):
        result = []
        for i in range(amount):
            result.append(self.cards.pop())
        return result
