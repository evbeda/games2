from collections import defaultdict

# Stages
PREFLOP = 0
FLOP = 1
TURN = 2
RIVER = 3
SHOWDOWN = 4

FIRST = 'first'
SECOND = 'second'
EQUAL = 'equal'

# Actions
NONE = 'none'
CHECK = 'check'  # pasar
CALL = 'call'  # igualar
RAISE = 'raise'  # aumentar una apuesta
BET = 'bet'  # apostar sin que nadie haya apostado antes
FOLD = 'fold'  # Abandonar

# Players
PLAYER = 'player'
CPU = 'cpu'

# Hierarchy
ROYAL_FLUSH = 'royal flush'
STRAIGHT_FLUSH = 'straight flush'
POKER = 'poker'
FULL_HOUSE = 'full house'
FLUSH = 'flush'
STRAIGHT = 'straight'
SET = 'set'
DOUBLE_PAIR = 'double pair'
PAIR = 'pair'
HIGH_CARD = 'high card'

greater_combinations = {
    ROYAL_FLUSH: 10,
    STRAIGHT_FLUSH: 9,
    POKER: 8,
    FULL_HOUSE: 7,
    FLUSH: 6,
    STRAIGHT: 5,
    SET: 4,
    DOUBLE_PAIR: 3,
    PAIR: 2,
    HIGH_CARD: 1,
}

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


def transform_cards_to_str(cards):
    aux = []
    for card in cards:
        aux.append(card.__repr__())
    return aux


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
        if(cardsDictionary[cardKey] == 3):
            result['trio'].append(cardKey)
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


def compare_combinations(first_comb, second_comb):
    sorted_first_comb = sort_cards_by_number(first_comb)
    sorted_second_comb = sort_cards_by_number(second_comb)
    for i in range(len(sorted_first_comb)):
        if sorted_first_comb[i] > sorted_second_comb[i]:
            return FIRST
        elif sorted_first_comb[i] < sorted_second_comb[i]:
            return SECOND
    return EQUAL


def better_hand(combinations):
    # 5 x 21 cards
    best_category = HIGH_CARD
    best_hand = combinations[0]
    for combination in combinations:
        category = best_category_combination(combination)
        if greater_combinations[category] >= greater_combinations[best_category]:
            best_category = category
            if compare_combinations(combination, best_hand) == FIRST:
                best_hand = combination
    return best_category, best_hand


def best_category_combination(combination):
    card = 0
    repetead_cards = {
        'poker': set([]),
        'trio': set([]),
        'par': set([])
    }
    repetead_cards['poker'] = set([])
    repetead_cards['trio'] = set([])
    repetead_cards['par'] = set([])
    for key, cards in find_repeated_cards(combination).items():
        for card in cards:
            repetead_cards[key].add(card)
    if find_royal_flush(combination):
        return ROYAL_FLUSH
    elif find_straight_flush(combination):
        return STRAIGHT_FLUSH
    elif len(repetead_cards['poker']) > 0:
        return POKER
    elif len(repetead_cards['trio']) == 1 and len(repetead_cards['par']) == 1:
        return FULL_HOUSE
    elif find_flush(combination):
        return FLUSH
    elif find_straight(combination):
        return STRAIGHT
    elif len(repetead_cards['trio']) > 0:
        return SET
    elif len(repetead_cards['par']) == 2:
        return DOUBLE_PAIR
    elif len(repetead_cards['par']) == 1:
        return PAIR
    return HIGH_CARD


def compare_hands(player_hand, cpu_hand):
    if greater_combinations[player_hand[0]] > greater_combinations[cpu_hand[0]]:
        return 'PLAYER WINS!'
    elif greater_combinations[player_hand[0]] < greater_combinations[cpu_hand[0]]:
        return 'CPU WINS!'
    else:
        winner = compare_combinations(player_hand[1], cpu_hand[1])
        if winner == FIRST:
            return 'PLAYER WINS!'
        elif winner == SECOND:
            return 'CPU WINS!'
        else:
            return 'TIE'
