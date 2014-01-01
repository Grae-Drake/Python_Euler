# Problem 10: Summation of primes

import math

def primeSieve(limit):
    
    # Returns a list of prime numbers below limit.
    array = [True for x in (range(limit))]      # Initialize array of booleans.
    root = math.ceil(limit ** .5)
    counter = 2                                 # Start sieving with number 2.
    result = []
    while counter <= root:
        if array[counter] == True:
            # Step through array and replace multiples of each prime number with False.
            array[counter * 2::counter] = [False for x in range(len(array[counter * 2::counter]))]
        counter += 1
    for x, y in enumerate(array):
        if y and x > 1:
            result.append(x)
    return result

def main(limit):

    # Returns the sum of all prime numbers below limit.
    return sum(primeSieve(limit))
print main(2000000)
