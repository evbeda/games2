class Player(object):
    def __init__(self, name):
        self.name = name
        self.combinations = []
        self.score = 0

    def choose_combination(self, combination):
        if combination not in self.combinations:
            self.combinations.append(combination)
