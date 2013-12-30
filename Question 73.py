    # Problem 73: Counting fractions in a range
    # How many fractions lie between 1/3 and 1/2 in the sorted list of
    # reduced proper fractions for d <= 12,000

from __future__ import division
import time, math, Euler
t1 = time.clock()

def factorize(limit):
    # Returns a list of numbers from 2 to and including
    # limit along with each number's unique prime factors.
    # This is a modified sieve of Eratosthenes.
    
    array = [[x,[]] for x in range(2,limit+1)]
    for item in array:
        value = item[0]
        factors = item[1]
        primeness = len(factors) == 0
        for multiple in range((value), limit+1, value):
            if primeness:
                array[multiple-2][1].append(value)
    return array

limit = 12000
table = factorize(limit)
my_dict = {key: value for (key, value) in table}
t2 = time.clock()

    # Now that we have a list of numbers and prime factors, it's time
    # to count the reduced proper fractions for each denominator in
    # the target range.

count = 0    
for item in table:
    denom = item[0]
    factors1 = item[1]
    floor = int((denom / 3)+1)
    if denom % 2 == 0:
        ceiling = int((denom / 2))
    else:
        ceiling = int((denom / 2)+ 1)
    for numer in range(floor, ceiling):
        factors2 = my_dict[numer]
        if len(list(set(factors1) & set(factors2))) == 0:
            count += 1

print count

t3 = time.clock()

print "Factor time: ", str(t2-t1)
print "Fraction time:", str(t3-t2)
