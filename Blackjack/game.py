from . import cardsDictionary, colorDictionary, cards_colors
from .player import Player
from .deck import Deck
from .hand import Hand

messages_who_win = {
    'Dealer': 'Dealer Wins!',
    'Player': 'Player Wins!',
    'T': 'TIE!',
    'C': 'CONTINUE',
}


class Game():
    name = 'Blackjack'
    input_args = 1

    def __init__(self):
        self.min_bet = 0
        self.player = None
        self.dealer_hand = None  # have to be a Hand
        self.pot = 0
        self.is_playing = True
        self.is_finished = True
        self.deck = Deck(cardsDictionary, colorDictionary)
        self.bet = 0
        self.bet_time = True
        self.start_game()

    def start_game(self):
        name = 'Martin'
        buy_in = 100
        self.min_bet = 5
        self.player = Player(name, buy_in)
        self.reset_round()

    def reset_round(self):
        player_hand = Hand()
        self.dealer_hand = Hand()
        player_hand.deal_card(self.deck.deal(2))
        self.dealer_hand.deal_card(self.deck.deal(2))
        self.player.hand = player_hand

    def check_you_can_bet(self):
        if self.player.money >= self.min_bet:
            return True
        else:
            self.is_playing = False
            return False

    def check_bet(self, bet):
        if bet > self.player.money:
            return 'You dont have enough money'
        elif bet < self.min_bet:
            return 'The bet is too low, the min bet is ' + str(self.min_bet)
        else:
            return 'NEW ROUND!'

    def give_money_to_winner(self, who):
        if who == 'Dealer Wins!':
            self.player.money -= self.bet
            if self.player.money == 0:
                self.is_playing = False
        elif who == 'Player Wins!':
            self.player.money += self.bet

    def who_wins(self):
        if self.dealer_hand.value == 21 and len(self.dealer_hand.cards) == 2:
            if (self.player.hand.value == 21 and
                    len(self.player.hand.cards) == 2):
                self.is_finished = True
                return messages_who_win['T']
            self.is_finished = True
            return messages_who_win['Dealer']
        elif self.player.hand.value == 21 and len(self.player.hand.cards) == 2:
            self.is_finished = True
            return messages_who_win['Player']
        elif self.dealer_hand.value > 21:
            self.is_finished = True
            return messages_who_win['Player']
        elif self.player.hand.value > 21:
            self.is_finished = True
            return messages_who_win['Dealer']
        elif self.dealer_hand.value == 21:
            self.is_finished = True
            return messages_who_win['Dealer']
        elif self.player.hand.value == 21:
            self.is_finished = True
            return messages_who_win['Player']
        elif (
            self.dealer_hand.value >= 17 and
            self.player.hand.value > self.dealer_hand.value
        ):
            self.is_finished = True
            return messages_who_win['Player']
        elif (
            self.dealer_hand.value >= 17 and
            self.dealer_hand.value > self.player.hand.value
        ):
            self.is_finished = True
            return messages_who_win['Dealer']
        elif (
                self.dealer_hand.value >= 17 and
                self.dealer_hand.value == self.player.hand.value
        ):
            self.is_finished = True
            return messages_who_win['T']
        elif self.dealer_hand.value < 17:
            self.is_playing = True
            return messages_who_win['C']

    def next_turn(self):
        if self.is_playing:
            if self.is_finished:
                return 'Enter your bet or q(quit)'
            else:
                return ('Do you want to stop (=) '
                        'or have another card (+)?, q to quit')
        else:
            return 'Game Over'

    @property
    def board(self):
        if not self.bet_time:
            dealer_cards = []
            player_cards = []
            for card in self.dealer_hand.cards:
                if(card[0] == 'T'):
                    dealer_cards.append('10' + cards_colors[card[1]])
                else:
                    dealer_cards.append(card[0] + cards_colors[card[1]])

            for card in self.player.hand.cards:
                if(card[0] == 'T'):
                    player_cards.append('10' + cards_colors[card[1]])
                else:
                    player_cards.append(card[0] + cards_colors[card[1]])

            return ('\n\nDealer: {dealer_cards}'
                    '\nPlayer: {player_cards}\n'
                    'Money: {player_money} \n\n').format(
                dealer_cards=dealer_cards,
                player_cards=player_cards,
                player_money=self.player.money,
            )
        else:
            return ''

    def play(self, command):
        if not self.check_you_can_bet():
            self.is_playing = False
            return 'You dont have money.'
        elif self.is_finished:
            if command == 'q':
                self.bet_time = True
                self.is_playing = False
                return 'You left the game'
            try:
                self.bet_time = True
                bet = int(command)
                result = self.check_bet(bet)
                if result == 'NEW ROUND!':
                    self.reset_round
                    self.bet = bet
                    self.is_finished = False
                    self.bet_time = False
                    self.reset_round()
                return result
            except Exception:
                return 'Please enter a number or q to quit'
        else:
            if command == '=':
                if self.who_wins() == 'CONTINUE':
                    self.dealer_hand.deal_card(self.deck.deal(1))
                    return self.play('=')
                else:
                    who_wins = self.who_wins()
                    self.give_money_to_winner(who_wins)
                    return who_wins
            elif command == '+':
                self.player.hand.deal_card(self.deck.deal(1))
                if self.who_wins() == 'CONTINUE':
                    who_wins = self.who_wins()
                    self.give_money_to_winner(who_wins)
                    return who_wins
                else:
                    who_wins = self.who_wins()
                    self.give_money_to_winner(who_wins)
                    return who_wins
            elif command == 'q':
                self.is_playing = False
                return 'You left the game'
            else:
                return 'Wrong command, please use + or = .'
