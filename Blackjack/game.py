
class Game():
    def __init__(self, min_bet, player):
        self.min_bet = min_bet
        self.player = player

    def check_you_can_bet(self):
        if self.player.money >= (self.min_bet * 2):
            return True
        else:
            return False
