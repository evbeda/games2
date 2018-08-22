class Player():
    def __init__(self, name):
        self.name = name
        self.hiddenCards = []
        self.score = []
        self.playedCards = []
    
    def play_card(self, index):
        playedCard = self.hiddenCards.pop(index)
        self.playedCards.append(playedCard)