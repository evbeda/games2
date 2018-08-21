class Hand():
    def __init__(self,mazo):
        self.mazo = mazo
        self.playersCards = {'1': [], '2': []}
    
    def deal_cards(self):
        
        self.playersCards['1'].append(self.mazo[0])
        self.playersCards['1'].append(self.mazo[1])
        self.playersCards['2'].append(self.mazo[2])
        self.playersCards['2'].append(self.mazo[3])

        # Sacar del mazo las 4 primeras cartas ya repartidas
        for i in range(3):
            self.mazo.pop(i-1)

            

    