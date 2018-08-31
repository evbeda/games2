import unittest

from .test_canto import TestCantos
from .test_cards import TestCards
from .test_deck import TestDeck
from .test_game import TestGame


class TestHand(unittest.TestCase):

    def test_hand_1(self):
        hand = Hand()
        # jugador1 tiene 3 cartas
        # jugador2 tiene 3 cartas
        # jugador1 sin cartas destapadas?
        # jugador2 sin cartas destapadas?
        # puntos en juego 0 ?
        # es mano 1?
        # es fase envido ?
        # ---
        # jugador 1 tira carta
        # es mano 1?
        # es fase envido ?
        # jugador1 tiene 2 cartas
        # jugador1 1 cartas destapada?
        # jugador2 tiene 3 cartas
        # jugador2 sin cartas destapadas?

    def test_hand_2(self):
        hand = Hand()
        # jugador 1 tira carta
        # jugador 2 tira carta
        # ---
        # jugador1 tiene 2 cartas
        # jugador2 tiene 2 cartas
        # jugador1 1 cartas destapada?
        # jugador2 1 cartas destapada?
        # no es fase envido ?
        # puntos en juego 0 ?
        # es mano 2?

    def test_hand_3(self):
        hand = Hand()
        # jugador 1 tira carta
        # jugador 2 tira carta
        # jugador 1 tira carta
        # jugador 2 tira carta
        # ---
        # jugador1 tiene 1 cartas
        # jugador2 tiene 1 cartas
        # jugador1 2 cartas destapadas?
        # jugador2 2 cartas destapadas?
        # no es fase envido ?
        # puntos en juego 0 ?
        # es mano 3?

    def test_hand_final(self):
        hand = Hand()
        # jugador 1 tira carta
        # jugador 2 tira carta
        # jugador 1 tira carta
        # jugador 2 tira carta
        # jugador 1 tira carta
        # jugador 2 tira carta
        # ---
        # jugador1 tiene 0 cartas
        # jugador2 tiene 0 cartas
        # jugador1 3 cartas destapadas?
        # jugador2 3 cartas destapadas?
        # no es fase envido ?
        # puntos en juego 0 ?
        # es fin de mano?


if __name__ == "__main__":
    unittest.main()
