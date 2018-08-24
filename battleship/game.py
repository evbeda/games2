from battleship.player import Player


class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def get_players(self):
        return [self.player1, self.player2]
