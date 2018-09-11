import random


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0


class HumanPlayer(Player):
    pass


class CPUPlayer(Player):

    def sort_already_envidos(self, already_envidos):
        envido_sorted = ['ENVIDO', 'ENVIDO', 'REAL ENVIDO',
                         'FALTA ENVIDO', ]
        aux = None
        for i in already_envidos:
            if aux == None:
                aux = envido_sorted.find(i)
            elif (aux < envido_sorted.find(i)):
                aux = envido_sorted.find(i)

    def ask_envido(self, already_envidos):
        possible_actions = self.choose_one_action(already_envidos)
        result = random.choice(possible_actions)
        return result

    def ask_trucos(self, already_trucos):
        truco_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'VALE CUATRO' in already_trucos:
            return random.choice(truco_possibles)
        truco_possibles.append('VALE CUATRO')
        if 'RE TRUCO' in already_trucos:
            return random.choice(truco_possibles)
        truco_possibles.append('RE TRUCO')
        return random.choice(truco_possibles)


    def choose_one_action(self, already_envidos):
        envido_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'FALTA ENVIDO' in already_envidos:
            return envido_possibles
        envido_possibles.append('FALTA ENVIDO')
        if 'REAL ENVIDO' in already_envidos:
            return envido_possibles
        envido_possibles.append('REAL ENVIDO')
        envidos = len([e for e in already_envidos if e == 'ENVIDO'])
        if envidos < 2:
            envido_possibles.append('ENVIDO')
        return envido_possibles

    def cpu_play(self):
        return random.choice(['ENVIDO', 'JUGAR', 'TRUCO'])
