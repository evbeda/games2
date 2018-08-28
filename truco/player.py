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

    def get_name(self):
        return self.name

    def is_hand(self):
        return self.is_hand

    def show_hand_to_board(self):
        hidden = ''
        played = ''
        for i in self.hiddenCards:
            hidden += i.__str__()
            hidden += ', '
        for i in self.playedCards:
            played += i.__str__()
            played += ', '
        return "Cartas en mano: {} \n {}{}".format(
            hidden,
            "Cartas jugadas: ",
            played
        )
