import random


def throwDice(num):
    results = []
    for number in range(0, num):
        results.append(random.randint(1, 6))
    return results
