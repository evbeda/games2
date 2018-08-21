from mazo import cardsDictionary
# import pdb; pdb.set_trace()

def sum_cards(cards):
    result = 0
    # Recorrer el array de cartas para colocar las As al final
    for index,card in enumerate(cards):
        if(card== 'A'):
            if(not(index+1 == len(cards))):
                cards.append(cards.pop(index))

    for card in cards:
        if(card == 'A'):
            # Si el As con valor 11, da un resultado mayor a 21
            if( (result + cardsDictionary[card][1]) > 21):
                # Usar el As como 1
                result += cardsDictionary[card][0]
            else:
                # Usar el As como 11
                result += cardsDictionary[card][1]
        else:
            result += cardsDictionary[card]
    return result

def compare_bet(min_bet,bet):
    if(bet >= min_bet):
        return True
    else:
        return False
