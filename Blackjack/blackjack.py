from .mazo import cardsDictionary
# import pdb; pdb.set_trace()

def compare_bet(min_bet, bet):
    if(bet >= min_bet):
        return True
    else:
        return False
