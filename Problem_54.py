        # Problem 54: Poker hands
from poker_functions import*

f = open("poker.txt")
biglist = f.readlines()
f.close()
biglist = [[[''.join(x[:15:3]),''.join(x[1:15:3])],
            [''.join(x[15:-1:3]),''.join(x[16:-1:3])]] for x in biglist]
testlist = biglist[:3]

# The format for biglist is [[['8TK94', 'CSCHS'], ['7253A', 'DSDSC']], ...]
# Player 1's first hand is biglist[0][0].  His card values are biglist[0][0][0] and
# his card suits are biglist[0][0][1].


def compare_hands(match):
    p1cards = match[0][0]
    p1suits = match[0][1]
    p2cards = match[1][0]
    p2suits = match[1][1]
    
    p1hand = [flush_check(p1suits),             # 0. Check for a flush
              straight_check(p1cards),          # 1. Check for a straight
              four_of_a_kind_check(p1cards),    # 2. Check for four of a kind
              full_house_check(p1cards),        # 3. Check for a full house
              three_of_a_kind_check(p1cards),   # 4. Check for three of a kind
              two_pair_check(p1cards),          # 5. Check for two pair
              pair_check(p1cards),              # 6. Check for a single pair
              high_card_check(p1cards)]         # 7. Check high cards

    p2hand = [flush_check(p2suits),
              straight_check(p2cards),
              four_of_a_kind_check(p2cards),
              full_house_check(p2cards),
              three_of_a_kind_check(p2cards),
              two_pair_check(p2cards),
              pair_check(p2cards),
              high_card_check(p2cards)]
    print(p1hand)
    print(p2hand)

print(biglist[11])
compare_hands(biglist[11])














              
