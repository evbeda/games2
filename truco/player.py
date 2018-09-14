import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0


class HumanPlayer(Player):
    pass


class CPUPlayer(Player):

    def ask_envido(self, already_envidos):
        possible_actions = self.choose_one_action(already_envidos)
        result = random.choice(possible_actions)
        return result

    def ask_trucos(self, already_trucos):
        truco_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'VALE_CUATRO' in already_trucos:
            return random.choice(truco_possibles)
        truco_possibles.append('VALE_CUATRO')
        if 'RE_TRUCO' in already_trucos:
            return random.choice(truco_possibles)
        truco_possibles.append('RE_TRUCO')
        return random.choice(truco_possibles)

    def choose_one_action(self, already_envidos):
        envido_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'FALTA_ENVIDO' in already_envidos:
            return envido_possibles
        envido_possibles.append('FALTA_ENVIDO')
        if 'REAL_ENVIDO' in already_envidos:
            return envido_possibles
        envido_possibles.append('REAL_ENVIDO')
        envidos = len([e for e in already_envidos if e == 'ENVIDO'])
        if envidos < 2:
            envido_possibles.append('ENVIDO')
        return envido_possibles

    def cpu_play(self, possibles):
        return random.choice(possibles)
