# Problem 14: Longest Collatz sequence  

import time
t1 = time.clock()

def getSequenceLength(n):

    # Returns the number of elements in n's Collatz sequence
    counter = 1
    var = n
    while var != 1:
        if var % 2 == 0:
            var = var/2
            counter += 1
        else:
            var = 3 * var + 1
            counter += 1
    return counter

def main(limit):

    # Returns the number less than limit with the longest Collatz sequence
    result = 0
    longestSequence = 0
    for n in range(1,limit):
        sequenceLength = getSequenceLength(n)
        if sequenceLength > longestSequence:
            longestSequence = sequenceLength
            result = n
    return result
    
print main(1000000)

print "Execution time: " + str(time.clock() - t1) + " seconds"