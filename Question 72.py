    # Problem 72: Counting fractions
    # Note: answer for 100 should be 304191

import time, math, Euler
t1 = time.clock()

def factorize(limit):
    array = [[x,[]] for x in range(2,limit)]

    for item in array:
        value = item[0]
        factors = item[1]
        primeness = len(factors) == 0
        for multiple in range((value), limit, value):
            if primeness:
                array[multiple-2][1].append(value)
    return array

limit = 1000000

table = factorize(limit +1)

t2 = time.clock()

counter = 0
for item in table:
    value = item[0]
    factors = item[1]
    total = value
    for factor1 in factors:
        total -= value/factor1
        for factor2 in factors:
            if factor2 > factor1:
                total += (value/(factor1*factor2))
                for factor3 in factors:
                    if factor3 > factor2:
                        total -= value/(factor1*factor2*factor3)
                        for factor4 in factors:
                            if factor4> factor3:
                                total += value/(factor1*factor2*factor3*factor4)
                                for factor5 in factors:
                                    if factor5 > factor4:
                                        total -= value/(factor1*factor2*factor3*factor4*factor5)
                                        for factor6 in factors:
                                            if factor6 > factor5:
                                                total += value/(factor1*factor2*factor3*factor4*factor5*factor6)
                                                for factor7 in factors:
                                                    if factor7 > factor6:
                                                        total -= value/(factor1*factor2*factor3*factor4*factor5*factor6*factor7)
    counter += total

print "Answer:", counter

t3 = time.clock()

print "Factor time: ", str(t2-t1)
print "Fraction time:", str(t3-t2)
