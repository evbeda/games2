from .player import Player


class Game():

    def __init__(self, name, name2):
        self.player1 = Player(name)
        self.player2 = Player(name2)

    def finished(self):
        if (
            len(self.player1.combinations) == 13 and
            len(self.player2.combinations) == 13
        ):
            return True
        else:
            return False
