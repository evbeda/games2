from collections import defaultdict

def encontrarEscaleraReal(cards):
    initialSuit = cards[0][1:]
    for card in cards:
        suit = card[1:]
        value = card[:1]
        if (value == "A" or value == "K" or value == "Q" or value == "J" or value == "T") and suit == initialSuit:
            continue
        else:
            return False
    return True
