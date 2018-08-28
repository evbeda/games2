import random


class Throw(object):

    def __init__(self):
        self.number = 0
        self.dice = []
        self.roll([0, 1, 2, 3, 4, ])

    def roll(self, which):
        self.number += 1
        if not self.is_possible_to_roll():
            return "Error. Max roll number reached."
        for i in which:
            if len(self.dice) == 5:
                self.dice[i] = random.randint(1, 6)
            else:
                self.dice.append(random.randint(1, 6))

    def is_possible_to_roll(self):
        if self.number > 3:
            return False
        else:
            return True
