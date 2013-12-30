# These are the poker functions used with problem 54.

def convert(hand):
    # Converts a string like '23TAK' to [2, 3, 10, 14, 13].
    values = {x:i for i,x in enumerate("0123456789TJQKA")}
    answer = []
    hand = str(hand)
    for x in hand:
        answer.append(values[x])
    return answer

def flush_check(suits):
    # Returns [True, [high_card]] if each character in argument is the same,
    # otherwise returns [False, []].
    return suits == suits[0]*len(suits)

def straight_check(hand):
    # Returns [True,[high_card]] if all cards in hand are consecutive values,
    # otherwise returns [False, []].
    if type(hand) == str:
        hand = convert(hand)
    for x in hand:
        hand = sorted(hand)
    straight = True
    for index, card in enumerate(hand[:-1]):
        if hand[index+1] != card+1:
            straight = False
    if straight == True:
        return [straight, high_card_check(hand)]
    else:
        return [straight, []]

def four_of_a_kind_check(hand):
    # Checks to see if hand contains four of a kind.  If so it returns[x,y]
    # where x is the value of the quadrupple and y is the remaining card.
    # If there is not a four of a kind, this function returns [False, []].
    if type(hand) == str:
        hand = convert(hand)
    hand = sorted(hand, reverse=True)
    if hand.count(hand[0]) == 4:
        return [hand[0], hand[-1]]
    elif hand.count(hand[-1]) == 4:
        return [hand[-1], hand[0]]
    else:
        return [False, []]



def full_house_check(hand):
    # Checks to see if hand consists of a full house.  If so it returns [x,y]
    # where x is the value of the tripple and y is the value of the double.
    # If there is not a full house, this function returns [False, []].
    if type(hand) == str:
        hand = convert(hand)
    hand = sorted(hand, reverse=True)
    if (hand.count(hand[0]) == 2) and (hand.count(hand[-1]) == 3):
        return [hand[-1], hand[0]] 
    elif (hand.count(hand[-1]) == 2) and (hand.count(hand[0]) == 3):
        return [hand[0], hand[-1]] 
    else:
        return [False, []]

def three_of_a_kind_check(hand):
    # Checks to see if hand contains three of a kind.  If so it returns [x,y]
    # where x is a sorted list with the value of the tripple (e.g. threes.)
    # and y is the list returned by high_card_check on the remaining three cards.
    # If there are not three of a kind, this function returns [False,[]].
    others = []
    duplicate = []
    if type(hand) == str:
        hand = convert(hand)
    for x in hand:
        if x in others:
            duplicate.append(x)
        else:
            others.append(x)
    if len(set(hand)) == len(hand)-2 and len(set(duplicate)) == 1:
        others = list(filter(lambda x: x not in duplicate, others))
        return [duplicate[0], [high_card_check(others)]]
    else:
        return [False, []]
    

def two_pair_check(hand):
    # Checks to see if hand contains two pair.  If so it returns [x,y] where
    # x is a sorted list with the value of the pair (e.g. sixes and fives, etc.)
    # and y is the remaining card.  If there are not two pair, this function
    # returns [False,[]].
    others = []
    duplicate = []
    if type(hand) == str:
        hand = convert(hand)
    for x in hand:
        if x in others:
            duplicate.append(x)
        else:
            others.append(x)
    if len(duplicate) == 2:
        others = list(filter(lambda x: x not in duplicate, others))
        return [sorted(duplicate, reverse = True), others]
    else:
        return [False,[]]

def pair_check(hand):
    # Checks to see if hand contains one pair.  If so it returns [x,y] where
    # x is the value of the pair (e.g. sixes, eights, etc.) and y is the list
    # returned by high_card_check on the remaining three cards.  If there is no pair,
    # this function returns [False,[]].
    others = []
    duplicate = []
    if type(hand) == str:
        hand = convert(hand)
    if len(set(hand)) == len(hand)-1:
        for x in hand:
            if x in others:
                duplicate.append(x)
            else:
                others.append(x)
    others = list(filter(lambda x: x not in duplicate, others))
    if len(duplicate) > 0:
        return [duplicate[0], high_card_check(others)]
    else:
        return [False,[]]

    
def high_card_check(hand):
    # Returns an ordered list of the cards in hand from high to low.
    # Output format is: [14, 10, 10, 4, 5]
    if type(hand) == str:
        hand = convert(hand)
    return sorted(hand, reverse=True)    
