from collections import defaultdict

PREFLOP = 0
FLOP = 1
TURN = 2
RIVER = 3
SHOWDOWN = 4

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


def sort_cards_by_number(cards):
    # Obtiene cartas con la pinta y devuelve un array con los numeros ordenados
    numbers = []
    for card in cards:
        if card[0] == 'A':
            numbers.append(14)
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
        return 14
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

def get_face(card):
    if (card == 14):
        return 'A'
    elif (card == 10):
        return 'T'
    elif (card == 11):
        return 'J'
    elif (card == 12):
        return 'Q'
    elif (card == 13):
        return 'K'
    else:
        return card
def find_royal_flush(cards):
    numbers = sort_cards_by_number(cards)
    # Escalera con AS,10,J,Q,K
    if numbers == [10, 11, 12, 13, 14] and find_flush(cards):
        return True
    else:
        return False


def find_repeated_cards(cards):
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


def find_flush(cards):
    color = cards[0][1]
    for card in cards:
        if card[1] != color:
            return False
    return True


def find_straight(cards):
    numbers = sort_cards_by_number(cards)
    # Escalera con AS,10,J,Q,K
    if numbers == [10, 11, 12, 13, 14]:
        return True
    elif numbers == [2, 3, 4, 5, 14]:
        return True
    for i in range(len(numbers) - 1):
        if (numbers[i + 1] - numbers[i]) != 1:
            return False
    return True


def find_straight_flush(cards):
    if find_flush(cards) and find_straight(cards):
        return True
    else:
        return False


def find_cards_suits(cards):
    numbers = sort_cards_by_number(cards)
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
    repetead_cards = {
        'poker': set([]),
        'trio': set([]),
        'par': set([])
    }
    for combination in combinations:
        for key, cards in find_repeated_cards(combination).items():
            for card in cards:
                repetead_cards[key].add(card)
        if find_royal_flush(combination):
            return "Escalera Real"
        elif find_straight_flush(combination):
            return "Escalera Color"
        elif len(repetead_cards['poker']) > 0:
            return "Poker"
        if len(repetead_cards['trio']) > 0:
            for trio in repetead_cards['trio']:
                if (get_value(trio) > greater_set):
                    greater_set = get_value(trio)
        if len(repetead_cards['par']) > 0:
            for pair in repetead_cards['par']:
                if get_value(pair) > greater_pair:
                    greater_pair = get_value(pair)
    if (len(repetead_cards['trio']) > 0 and len(repetead_cards['par']) > 0):
        if greater_pair != greater_set:
            return 'Full House de {} y {}'.format(get_face(greater_set), get_face(greater_pair))
        else:
            repetead_cards['par'].discard(str(get_face(greater_set)))
            second_best_pair = max(repetead_cards['par'])
            return 'Full House de {} y {}'.format(get_face(greater_set), get_face(second_best_pair))
    if (greater_set > 0):
        return 'Trio de {}'.format(get_face(greater_set))
    if (greater_pair > 0):
        return 'Par de {}'.format(get_face(greater_pair))
