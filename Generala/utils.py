import random

from . import *


def throw_dice(num):
    results = []
    for number in range(0, num):
        results.append(random.randint(1, 6))
    return results

def check_throw(throw_array, points_to_check, throw_number):
    if points_to_check == GENERALA:
        if throw_number != 1:
            for index in range(0, len(throw_array) - 1):
                if throw_array[index] != throw_array[index + 1]:
                    return False
            return True
        elif throw_number == 1:
            return False
    if points_to_check == GENERALASERVIDA:
        if throw_number != 1:
            return False
        elif throw_number == 1:
            for index in range(0, len(throw_array) - 1):
                if throw_array[index] != throw_array[index + 1]:
                    return False
            return True
    elif points_to_check == POKER:
        for index in range(0, len(throw_array)):
            if throw_array.count(index + 1) == 4:
                return True
        return False
    elif points_to_check == FULL:
        if throw_array.count(1) == 3:
            if throw_array.count(2) == 2:
                return True
            elif throw_array.count(3) == 2:
                return True
            elif throw_array.count(4) == 2:
                return True
            elif throw_array.count(5) == 2:
                return True
            elif throw_array.count(6) == 2:
                return True
            else:
                return False
        elif throw_array.count(2) == 3:
            if throw_array.count(1) == 2:
                return True
            elif throw_array.count(3) == 2:
                return True
            elif throw_array.count(4) == 2:
                return True
            elif throw_array.count(5) == 2:
                return True
            elif throw_array.count(6) == 2:
                return True
            else:
                return False
        elif throw_array.count(3) == 3:
            if throw_array.count(1) == 2:
                return True
            elif throw_array.count(2) == 2:
                return True
            elif throw_array.count(4) == 2:
                return True
            elif throw_array.count(5) == 2:
                return True
            elif throw_array.count(6) == 2:
                return True
            else:
                return False
        elif throw_array.count(4) == 3:
            if throw_array.count(1) == 2:
                return True
            elif throw_array.count(3) == 2:
                return True
            elif throw_array.count(2) == 2:
                return True
            elif throw_array.count(5) == 2:
                return True
            elif throw_array.count(6) == 2:
                return True
            else:
                return False
        elif throw_array.count(5) == 3:
            if throw_array.count(1) == 2:
                return True
            elif throw_array.count(3) == 2:
                return True
            elif throw_array.count(4) == 2:
                return True
            elif throw_array.count(2) == 2:
                return True
            elif throw_array.count(6) == 2:
                return True
            else:
                return False
        elif throw_array.count(6) == 3:
            if throw_array.count(1) == 2:
                return True
            elif throw_array.count(3) == 2:
                return True
            elif throw_array.count(4) == 2:
                return True
            elif throw_array.count(5) == 2:
                return True
            elif throw_array.count(2) == 2:
                return True
            else:
                return False
        else:
            return False

    elif points_to_check == ESCALERA:
        orderedList = sorted(throw_array)
        if orderedList in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6],):
            return True
        else:
            return False
    elif 1 <= points_to_check <= 6:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == points_to_check:
                sum += points_to_check
        return sum
