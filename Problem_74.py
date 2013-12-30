    # Problem 74: Digit factorial chains
    # How many chains, with a starting number below one million, contain
    # exactly sixty non-repeating terms?

import time
t1 = time.clock()

big_table = {}
count = 0

for number in range(1,1000000):
    series = [number]
    factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880} 
    while True:
        start_num = series[-1]
        next_num = sum([factorials[int(x)] for x in str(start_num)])
        if next_num in big_table:
            for index, value in enumerate(series):
                big_table[value] = len(series) + big_table[next_num] - index
                if big_table[value] == 60:
                    count += 1
            break
        elif next_num not in series:
            series.append(next_num)
        else:
            for index, value in enumerate(series):
                big_table[value] = len(series) - index
                if big_table[value] == 60:
                    count += 1
            break

print count

t2 = time.clock()

print "Execution time: ", str(t2-t1)
