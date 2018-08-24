from collections import defaultdict


def ordenar_cartas_numeros(cards):
    # Obtiene cartas con la pinta y devuelve un array con los numeros ordenados
    numbers = []
    for card in cards:
        if card[0] == 'A':
            numbers.append(1)
        elif card[0] == 'T':
            numbers.append(10)
        elif card[0] == 'J':
            numbers.append(11)
        elif card[0] == 'Q':
            numbers.append(12)
        elif card[0] == 'K':
            numbers.append(13)
        else:
            numbers.append(int(card[0]))
    numbers.sort()
    return numbers


def get_value(card):
    if card[0] == 'A':
        return 1
    elif card[0] == 'T':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    else:
        return int(card[0])


def encontrarEscaleraReal(cards):
    numbers = ordenar_cartas_numeros(cards)
    # Escalera con AS,10,J,Q,K
    if numbers == [1, 10, 11, 12, 13] and encontrar_color(cards):
        return True
    else:
        return False


def encontrar_iguales(cards):
    cardsDictionary = defaultdict(int)
    for card in cards:
        cardNumber = card[0]
        cardsDictionary[cardNumber] += 1
    result = {
        'poker': [],
        'trio': [],
        'par': [],
    }
    for cardKey in cardsDictionary:
        if(cardsDictionary[cardKey] == 4):
            result['poker'].append(cardKey)
            break
        if(cardsDictionary[cardKey] == 3):
            result['trio'].append(cardKey)
            break
        if(cardsDictionary[cardKey] == 2):
            result['par'].append(cardKey)
    return result


def encontrar_color(cards):
    color = cards[0][1]
    for card in cards:
        if card[1] != color:
            return False
    return True


def encontrar_escalera(cards):
    numbers = ordenar_cartas_numeros(cards)
    # Escalera con AS,10,J,Q,K
    if numbers == [1, 10, 11, 12, 13]:
        return True
    for i in range(len(numbers) - 1):
        if (numbers[i + 1] - numbers[i]) != 1:
            return False
    return True


def encontrar_escalera_color(cards):
    if encontrar_color(cards) and encontrar_escalera(cards):
        return True
    else:
        return False


def encontrar_cartas_pintas(cards):
    numbers = ordenar_cartas_numeros(cards)
    orderCards = []
    for number in numbers:
        for card in cards:
            if(get_value(card[0]) == number):
                orderCards.append(card)
    return orderCards
