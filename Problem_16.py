# Problem 16: Power digit sum

import time
t1 = time.clock()

def findDigitSum(n):
    return sum([int(x) for x in str(n)])

print findDigitSum(2**1000)
print "Execution time: " + str(time.clock() - t1) + " seconds."
