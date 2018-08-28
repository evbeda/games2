class Player():
    def __init__(self, name):
        self.name = name
        self.hidden_cards = []
        self.score = []
        self.played_cards = []
        self.is_hand = bool

    def play_card(self, index):
        played_card = self.hidden_cards.pop(index)
        self.played_cards.append(played_card)

    def reset_hand(self):
        del self.hidden_cards[:]
        del self.played_cards[:]

    def get_name(self):
        return self.name

    def show_hand_to_board(self):
        hidden = ''
        played = ''
        for i in self.hidden_cards:
            hidden += i.__str__()
            hidden += ', '
        for i in self.played_cards:
            played += i.__str__()
            played += ', '
        return "Cartas en mano: {} \n {}{}".format(
            hidden,
            "Cartas jugadas: ",
            played
        )
