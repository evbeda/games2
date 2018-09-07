from .deck import Deck

envido_combinations = [
    ['Envido', 2, 1],
    ['Real Envido', 3, 1],
    ['Falta Envido', 0, 1],
    ['Envido', 'Envido', 4, 2],
    ['Envido', 'Real Envido', 5, 2],
    ['Envido', 'Falta Envido', 0, 2],
    ['Envido', 'Envido', 'Real Envido', 7, 4],
    ['Envido', 'Envido', 'Falta Envido', 0, 4],
    ['Envido', 'Real Envido', 'Falta Envido', 0, 5],
    ['Envido', 'Envido', 'Real Envido', 'Falta Envido', 0, 7],
]


class Hand(object):

    def __init__(self):
        self.turn = 0
        self.points = 0
        self.number_hand = 1
        self.played_cards = None
        self.hidden_cards = None
        self.deal_cards()

    def deal_cards(self):
        self.hidden_cards = [[], [], ]
        self.played_cards = [[], [], ]
        deck = Deck()
        for player in range(2):
            for card_index in range(3):
                self.hidden_cards[player].append(deck.get_card())

    def play_card(self, card_index):
        played_card = self.hidden_cards[self.turn].pop(card_index)
        self.played_cards[self.turn].append(played_card)
        self.turn = 0 if (self.turn == 1) else 1

    def next_hand(self):
        if len(self.played_cards[0]) == len(self.played_cards[1]):
            self.number_hand += 1

    def who_is_next(self):
        if self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'GREATER':
            self.turn = 0
        elif self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'EQUAL':
            pass
        else:
            self.turn = 1

    @property
    def is_playing(self):
        if len(self.played_cards[0]) == len(self.played_cards[1]):
            win_hands = 0
            for i in range(len(self.played_cards[0])):
                if self.played_cards[0][i].compare_with(self.played_cards[1][i]) == 'GREATER':
                    win_hands += 1
            if win_hands >= 2:
                return False

    def get_score_envido(self, player):
        same_suit_cards = set()
        all_cards = self.hidden_cards[player] + self.played_cards[player]
        white = []
        for i in range(len(all_cards) - 1):
            for j in range(len(all_cards)):
                if i == j:
                    pass
                else:
                    if all_cards[i].suit == all_cards[j].suit:
                        same_suit_cards.add(all_cards[i].number)
                        same_suit_cards.add(all_cards[j].number)
        if len(same_suit_cards) == 0:
            for i in all_cards:
                if i.number > 8:
                    all_cards.remove(i)
            return 0 if (len(all_cards) == 0) else max(all_cards).number
        else:
            for card in same_suit_cards:
                if card < 8:
                    white.append(card)
            if len(white) == 0:
                return 20
            elif len(white) == 1:
                return white[0] + 20
            elif len(white) == 2:
                return white[0] + white[1] + 20
            elif len(white) == 3:
                card = max(white)
                white.remove(card)
                card_two = max(white)
                return card + card_two + 20

    @property
    def envido(self):
        return True

    def show_cards(self):
        result = []
        result.append('\nMis Cartas: \n')
        for card in self.hidden_cards[0]:
            result.append(str(card) + ' ')
        result.append('\nCartas jugadas: \n')
        for group in self.played_cards:
            for card2 in group:
                result.append(str(card2) + ' ')
        return ''.join(result)
