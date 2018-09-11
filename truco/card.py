from . import SWORD, COARSE, GOLD, CUP


class Card(object):
    hierarchical_deck = (
        ((SWORD, 1,),),
        ((COARSE, 1,),),
        ((SWORD, 7,),),
        ((GOLD, 7,),),
        ((SWORD, 3,), (COARSE, 3,), (GOLD, 3,), (CUP, 3,),),
        ((SWORD, 2,), (COARSE, 2,), (GOLD, 2,), (CUP, 2,),),
        ((GOLD, 1,), (CUP, 1,),),
        ((SWORD, 12,), (COARSE, 12,), (GOLD, 12,), (CUP, 12,),),
        ((SWORD, 11,), (COARSE, 11,), (GOLD, 11,), (CUP, 11,),),
        ((SWORD, 10,), (COARSE, 10,), (GOLD, 10,), (CUP, 10,),),
        ((COARSE, 7,), (CUP, 7,),),
        ((SWORD, 6,), (COARSE, 6,), (GOLD, 6,), (CUP, 6,),),
        ((SWORD, 5,), (COARSE, 5,), (GOLD, 5,), (CUP, 5,),),
        ((SWORD, 4,), (COARSE, 4,), (GOLD, 4,), (CUP, 4,),),
    )

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.position = self.get_position()

    def get_position(self):
        for i in range(len(self.hierarchical_deck)):
            for x in range(len(self.hierarchical_deck[i])):
                if (
                        self.suit == self.hierarchical_deck[i][x][0] and
                        self.number == self.hierarchical_deck[i][x][1]
                ):
                    return i

    def compare_with(self, card_two):
        if self.position < card_two.position:
            return 'GREATER'
        elif self.position == card_two.position:
            return 'EQUAL'
        else:
            return 'LOWER'

    def __str__(self):
        return "{} {}".format(self.number, self.suit)

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.number == other.number and self.suit == other.suit

    def __gt__(self, other):
        return self.number > other.number
