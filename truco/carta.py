from . import ESPADA, BASTO, ORO, COPA


class Carta():
    mazoJerarquico = (
        ((ESPADA, 1,),),
        ((BASTO, 1,),),
        ((ESPADA, 7,),),
        ((ORO, 7,),),
        ((ESPADA, 3,), (BASTO, 3,), (ORO, 3,), (COPA, 3,),),
        ((ESPADA, 2,), (BASTO, 2,), (ORO, 2,), (COPA, 2,),),
        ((ORO, 1,), (COPA, 1,),),
        ((ESPADA, 12,), (BASTO, 12,), (ORO, 12,), (COPA, 12,),),
        ((ESPADA, 11,), (BASTO, 11,), (ORO, 11,), (COPA, 11,),),
        ((ESPADA, 10,), (BASTO, 10,), (ORO, 10,), (COPA, 10,),),
        ((BASTO, 7,), (COPA, 7,),),
        ((ESPADA, 6,), (BASTO, 6,), (ORO, 6,), (COPA, 6,),),
        ((ESPADA, 5,), (BASTO, 5,), (ORO, 5,), (COPA, 5,),),
        ((ESPADA, 4,), (BASTO, 4,), (ORO, 4,), (COPA, 4,),),
    )

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.position = self.get_position()

    def get_position(self):
        for i in range(len(self.mazoJerarquico)):
            for x in range(len(self.mazoJerarquico[i])):
                if (
                    self.suit == self.mazoJerarquico[i][x][0] and
                    self.number == self.mazoJerarquico[i][x][1]
                ):
                    return i

    def compare_with(self, cartaDos):
        if self.position < cartaDos.position:
            return 'GREATER'
        elif self.position == cartaDos.position:
            return 'EQUAL'
        else:
            return 'LOWER'

    def __str__(self):
        return "{} {}".format(self.number, self.suit)

    def __eq__(self, other):
        if isinstance(other, Carta):
            return (self.number == other.number and self.suit == self.suit)
        return False
