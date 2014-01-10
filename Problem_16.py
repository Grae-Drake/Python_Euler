# Problem 16: Power digit sum

import time
t1 = time.clock()

def find_digit_sum(n):
    return sum([int(x) for x in str(n)])

print find_digit_sum(2**1000)
print "Execution time: " + str(time.clock() - t1) + " seconds."
