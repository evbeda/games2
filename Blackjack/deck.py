import random


class Deck( ):
    def __init__(self, values, suits):
        self.values = values
        self.suits = suits 
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(value + suit)

    def shuffle(self):
        random.shuffle(self.cards)    
