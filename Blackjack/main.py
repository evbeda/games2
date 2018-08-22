from player import Player
from game import Game
from hand import Hand
if __name__ == "__main__":
	#Este es un espacio para generar cartas aleatorias
    player1 = Player(10)
    game1 = Game(5, player1)
    if game1.check_you_can_play():
    	player1.money -= game1.min_bet
    	mano = Hand(['2', '3', '4', '5'])
    else:
    	print ('I am sorry,you do not have enough money')
