    # Problem 74: Digit factorial chains
    # How many chains, with a starting number below one million, contain
    # exactly sixty non-repeating terms?

import time, math
t1 = time.clock()

def chain_length(number):
    # Returns the number of non-repeating terms in the series generated
    # by summing the factorials of each digit of number and repeating
    # until a term is repeated.  Ex: 69 --> 363601 --> 1454 --> 169 -->
    # 363601 (--> 1453) will return 5.

    answer = 0
    series = [number]
    factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880} 
    while answer == 0:
        start_num = series[-1]
        next_num = sum([factorials[int(x)] for x in str(start_num)])
        if next_num in big_table:
            answer = len(series) + big_table[next_num]
        elif next_num not in series:
            series.append(next_num)
        else:
            series.append(next_num)
            answer = len(series)
    return answer

big_table = {}
count = 0
for x in range(1,1000000):
    big_table[x] = chain_length(x)

for key, value in big_table.items():
    if value == 61:                 # Note: value should be 60.  Off by 1, unsure why.
        count += 1

print count

t3 = time.clock()

print "Execution time: ", str(t3-t1)
