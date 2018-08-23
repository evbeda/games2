class Player():
    def __init__(self, name):
        self.name = name
        self.hiddenCards = []
        self.score = []
        self.playedCards = []
        self.is_hand = bool

    def play_card(self, index):
        playedCard = self.hiddenCards.pop(index)
        self.playedCards.append(playedCard)

    def reset_hand(self):
        del self.hiddenCards[:]
        del self.playedCards[:]
