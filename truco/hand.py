
from .deck import Deck

envido_combinations = [
    [['ENVIDO'], 2, 1],
    [['REAL ENVIDO'], 3, 1],
    [['FALTA ENVIDO'], 0, 1],
    [['ENVIDO', 'ENVIDO'], 4, 2],
    [['REAL ENVIDO', 'FALTA ENVIDO'], 5, 2],
    [['ENVIDO', 'REAL ENVIDO'], 5, 2],
    [['ENVIDO', 'FALTA ENVIDO'], 0, 2],
    [['ENVIDO', 'ENVIDO', 'REAL ENVIDO'], 7, 4],
    [['ENVIDO', 'ENVIDO', 'FALTA ENVIDO'], 0, 4],
    [['ENVIDO', 'REAL ENVIDO', 'FALTA ENVIDO'], 0, 5],
    [['ENVIDO', 'ENVIDO', 'REAL ENVIDO', 'FALTA ENVIDO'], 0, 7],
]

envido_posibilities = ["ENVIDO", "REAL ENVIDO", "FALTA ENVIDO"]


class Hand(object):

    def __init__(self, mano=0):
        self.turn = 0
        self.number_hand = 1
        self.played_cards = None
        self.hidden_cards = None
        self.envido_fase = True
        self.truco_fase = True
        self.winner_index = None
        self.mano = mano
        self.deal_cards()
        self.envidos = []

    def limpiar_mesa(self):
        self.hidden_cards = [[], [], ]
        self.played_cards = [[], [], ]
        self.winner_index = None

    def deal_cards(self):
        self.limpiar_mesa()
        deck = Deck()
        for player in range(2):
            for card_index in range(3):
                self.hidden_cards[player].append(deck.get_card())

    def play_card(self, card_index):
        played_card = self.hidden_cards[self.turn].pop(card_index)
        self.played_cards[self.turn].append(played_card)
        self.cambiar_turno()

    def cambiar_turno(self):
        self.turn = 0 if (self.turn == 1) else 1

    def siguiente_ronda(self):
        if len(self.played_cards[0]) == len(self.played_cards[1]):
            self.envido_fase = False
            self.number_hand += 1

    def who_is_next(self):
        if self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'GREATER':
            self.turn = 0
        elif self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'EQUAL':
            pass
        else:
            self.turn = 1

    def get_envido_points(self, won = 0):
        for combination in envido_combinations:
            if combination[0] == self.envidos:
                return combination[won + 1]

    def accept_envido(self):
        self.envido_fase = False

    def reject_envido(self):
        self.envido_fase = False
        self.envidos = []

    def sing_envido(self, command):
        if not self.envido_fase:
            raise Exception()
        self.envidos.append(command)

    @property
    def is_playing(self):
        win_hands_1 = 0
        win_hands_0 = 0
        for i in range(len(self.played_cards[0])):
            cartaPC = self.played_cards[1][i]
            cartaHumano = self.played_cards[0][i]
            if cartaHumano.compare_with(cartaPC) == 'GREATER':
                win_hands_0 += 1
            if cartaPC.compare_with(cartaHumano) == 'GREATER':
                win_hands_1 += 1
        if win_hands_0 is win_hands_1 and self.number_hand is 4:
            self.winner_index = self.mano
            return False
        if win_hands_0 >= 2 or win_hands_1 >= 2:
            self.winner_index = 0 if win_hands_0 > win_hands_1 else 1
            return False
        return True

    def get_envido_winner(self):
        score_p0 = self.get_score_envido(0)
        score_p1 = self.get_score_envido(1)
        if score_p0 > score_p1:
            return 0
        elif score_p0 < score_p1:
            return 1
        else:
            return self.mano

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


    def show_cards(self):
        result = []
        result.append('\nMis Cartas: \n')
        for card in self.hidden_cards[0]:
            result.append(str(card) + ' ')
        result.append('\nCartas jugadas: \n')
        contador = 0
        for group in self.played_cards:
            if contador == 0:
                result.append("H: ")
                contador += 1
            else:
                result.append("C: ")
            for card2 in group:
                result.append(str(card2) + ' ')
            result.append('\n')
        return ''.join(result)
