# Problem 23: Non-abundant sums

import time, math

t0 = time.clock()

def calc_proper_factors(x):

    # Returns a list of proper factors of x
    proper_factors = [[y, x/y] for y in range(2,int(math.sqrt(x) + 1)) if x % y == 0]
    proper_factors = sum(proper_factors, [])
    proper_factors.append(1)
    return set(proper_factors)  

def list_abundant_numbers(limit):

    # Returns a list of all abundant numbers below limit
    return [x for x in range(1,limit+1) if x < sum(calc_proper_factors(x))]
    
def list_non_abundant_sums(limit):
    
    # Returns a list of all numbers below limit that are not the sum of two
    # abundant numbers.  Could be improved with a sieving technique.
    result = []
    abundant_sums = {}
    abundant_numbers = list_abundant_numbers(limit)
    for index1, i in enumerate(abundant_numbers):
        for j in abundant_numbers[index1:]:
            if i + j < limit:
                abundant_sums[i + j] = True
            else:
                break
    for x in range(limit):
        if x not in abundant_sums.keys():
            result.append(x)
    return result

print sum(list_non_abundant_sums(28123))

print "Execution time: " + str(time.clock()-t0)[:4] + " seconds"

