from battleship.player import Player

game_states = ['init', 'war', 'finish']


class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.state = game_states[0]

    def get_players(self):
        return [self.player1, self.player2]

    def is_ready_to_war(self):
        if (
            self.player1.board_own.is_ready_to_war() and
            self.player2.board_own.is_ready_to_war()
        ):
            return True
        else:
            return False
