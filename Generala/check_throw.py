from . import *


def checkThrow(throwArray, pointsToCheck, throwNumber):
    if pointsToCheck == GENERALA:
        if throwNumber != 1:
            for index in range(0, len(throwArray) - 1):
                if throwArray[index] != throwArray[index + 1]:
                    return False
            return True
        elif throwNumber == 1:
            return False
    if pointsToCheck == GENERALASERVIDA:
        if throwNumber != 1:
            return False
        elif throwNumber == 1:
            for index in range(0, len(throwArray) - 1):
                if throwArray[index] != throwArray[index + 1]:
                    return False
            return True
    elif pointsToCheck == POKER:
        if throwArray.count(1) == 4:
            return True
        elif throwArray.count(2) == 4:
            return True
        elif throwArray.count(3) == 4:
            return True
        elif throwArray.count(4) == 4:
            return True
        elif throwArray.count(5) == 4:
            return True
        elif throwArray.count(6) == 4:
            return True
        else:
            return False
    elif pointsToCheck == FULL:
        if throwArray.count(1) == 3:
            if throwArray.count(2) == 2:
                return True
            elif throwArray.count(3) == 2:
                return True
            elif throwArray.count(4) == 2:
                return True
            elif throwArray.count(5) == 2:
                return True
            elif throwArray.count(6) == 2:
                return True
            else:
                return False
        elif throwArray.count(2) == 3:
            if throwArray.count(1) == 2:
                return True
            elif throwArray.count(3) == 2:
                return True
            elif throwArray.count(4) == 2:
                return True
            elif throwArray.count(5) == 2:
                return True
            elif throwArray.count(6) == 2:
                return True
            else:
                return False
        elif throwArray.count(3) == 3:
            if throwArray.count(1) == 2:
                return True
            elif throwArray.count(2) == 2:
                return True
            elif throwArray.count(4) == 2:
                return True
            elif throwArray.count(5) == 2:
                return True
            elif throwArray.count(6) == 2:
                return True
            else:
                return False
        elif throwArray.count(4) == 3:
            if throwArray.count(1) == 2:
                return True
            elif throwArray.count(3) == 2:
                return True
            elif throwArray.count(2) == 2:
                return True
            elif throwArray.count(5) == 2:
                return True
            elif throwArray.count(6) == 2:
                return True
            else:
                return False
        elif throwArray.count(5) == 3:
            if throwArray.count(1) == 2:
                return True
            elif throwArray.count(3) == 2:
                return True
            elif throwArray.count(4) == 2:
                return True
            elif throwArray.count(2) == 2:
                return True
            elif throwArray.count(6) == 2:
                return True
            else:
                return False
        elif throwArray.count(6) == 3:
            if throwArray.count(1) == 2:
                return True
            elif throwArray.count(3) == 2:
                return True
            elif throwArray.count(4) == 2:
                return True
            elif throwArray.count(5) == 2:
                return True
            elif throwArray.count(2) == 2:
                return True
            else:
                return False
        else:
            return False

    elif pointsToCheck == ESCALERA:
        orderedList = sorted(throwArray)
        if orderedList in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6],):
            return True
        else:
            return False
    elif 1 <= pointsToCheck <= 6:
        sum = 0
        for index in range(0, len(throwArray)):
            if throwArray[index] == pointsToCheck:
                sum += pointsToCheck
        return sum
