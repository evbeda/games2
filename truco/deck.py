import random

from . import SWORD, COARSE, GOLD, CUP
from .card import Card


class Deck(object):

    def __init__(self):
        self.ordered_deck = [
            Card(SWORD, 1), Card(COARSE, 1), Card(SWORD, 7),
            Card(GOLD, 7), Card(SWORD, 3), Card(
                COARSE, 3), Card(GOLD, 3), Card(CUP, 3),
            Card(SWORD, 2), Card(COARSE, 2), Card(GOLD, 2), Card(CUP, 2),
            Card(GOLD, 1), Card(CUP, 1),
            Card(SWORD, 12), Card(COARSE, 12), Card(GOLD, 12), Card(CUP, 12),
            Card(SWORD, 11), Card(COARSE, 11), Card(GOLD, 11), Card(CUP, 11),
            Card(SWORD, 10), Card(COARSE, 10), Card(GOLD, 10), Card(CUP, 10),
            Card(COARSE, 7), Card(CUP, 7),
            Card(SWORD, 6), Card(COARSE, 6), Card(GOLD, 6), Card(CUP, 6),
            Card(SWORD, 5), Card(COARSE, 5), Card(GOLD, 5), Card(CUP, 5),
            Card(SWORD, 4), Card(COARSE, 4), Card(GOLD, 4), Card(CUP, 4)
        ]

    def get_card(self):
        indice = random.randint(0, len(self.ordered_deck) - 1)
        aux = self.ordered_deck[indice]
        del self.ordered_deck[indice]
        return aux
