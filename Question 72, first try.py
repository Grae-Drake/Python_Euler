    # Problem 72: Counting fractions
    # Note: answer for 100 is 304191

import time, math, Euler

def get_factors(x):
    # Returns a sorted list of factors of x, excluding 1
    factors = []
    for y in primes:
        if x%y == 0:
            factors.append(y)

    factors.sort()
    return factors

t1 = time.clock()

limit = 100000
primes = Euler.primeSieve(limit)
t2 = time.clock()

table = {1: []}
counter = 0
for x in range(2,limit+1):
    table[x] = get_factors(x)

t3 = time.clock()

for x in range(2, limit+1):
    total = x
    for y in table[x]:
        total -= x/y
        for z in table[x]:
            if z > y:
                total += (x/(y*z))
    counter += total

print counter

t4 = time.clock()
print "Sieve time: ", str(t2-t1)
print "Table time: ", str(t3-t2)
print "Fraction time:", str(t4-t3)
print "Total time: ", t4-t1
