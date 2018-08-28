from collections import defaultdict


five_cards_combinations = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 5],
    [0, 1, 2, 3, 6],
    [0, 1, 2, 4, 5],
    [0, 1, 2, 4, 6],
    [0, 1, 2, 5, 6],
    [0, 1, 3, 4, 5],
    [0, 1, 3, 4, 6],
    [0, 1, 3, 5, 6],
    [0, 1, 4, 5, 6],
    [0, 2, 3, 4, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [0, 2, 4, 5, 6],
    [0, 3, 4, 5, 6],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 5, 6],
    [1, 2, 4, 5, 6],
    [1, 3, 4, 5, 6],
    [2, 3, 4, 5, 6],
]


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


def encontrar_escalera_real(cards):
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


def combine_card(complete_card):
    all_combination = []
    for index_combination in five_cards_combinations:
        card_combination = []
        for index in index_combination:
            card_combination.append(complete_card[index])
        all_combination.append(card_combination)
    return all_combination


def better_hand(combinations):
    greater_full = 0
    greater_flush = 0
    greater_straight = 0
    greater_set = 0
    greater_pair = 0
    card = ''
    for combination in combinations:
        iguales = encontrar_iguales(combination)
        if encontrar_escalera_real(combination):
            return "Escalera Real"
        elif encontrar_escalera_color(combination):
            return "Escalera Color"
        elif len(iguales['poker']) > 0:
            return "Poker"
        elif len(iguales['trio']) > 0:
            for trio in iguales['trio']:
                if (get_value(trio) > greater_set):
                    greater_set = get_value(trio)
    if (greater_set > 0):
        if (greater_set == 1):
            card = 'A'
        elif (greater_set == 10):
            card = 'T'
        elif (greater_set == 11):
            card = 'J'
        elif (greater_set == 12):
            card = 'Q'
        elif (greater_set == 13):
            card = 'K'
        else:
            card = greater_set
        return 'Trio de {}'.format(card)
        # TODO quitar el return y actualizar los test
    return "No es Escalera Real"
