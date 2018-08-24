from random import randint


class GuessNumberGame(object):

    def __init__(self):
        self._guess_number = randint(0, 100)
        self.played_numbers = []
        self.is_playing = True

    def next_turn(self):
        if self.is_playing:
            return 'Give me a number from 0 to 100'
        else:
            return 'Game Over'

    def play(self, number):
        self.played_numbers.append(number)
        if number < self._guess_number:
            return 'too low'
        elif number > self._guess_number:
            return 'too high'
        self.is_playing = False
        return 'you win'

    @property
    def board(self):
        return str(self.played_numbers)
