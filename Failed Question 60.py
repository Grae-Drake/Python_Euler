    # Problem 69: Prime pair sets
    
    # Find the lowest sum for a set of five primes for which any
    # two primes concatenate to produce another prime.

    # First group is [3, 7, 109, 673]
    # Other groups: [7, 19, 97, 3727], [11, 23, 743, 1871], [13, 19, 577, 28219],
    # [17, 83, 449, 362897]

import time
import Euler

t1 = time.clock()

def is_pair(x,y):
    # Returns True if xy and yx are each prime, else returns False
    
    test1 = int(str(x) + str(y))
    test2 = int(str(y) + str(x))
    return Euler.isPrime(test1) == True and Euler.isPrime(test2) == True 

prime_list = Euler.primeSieve(30000)
prime_table = {x: True for x in prime_list}

print(len(prime_list))
    
t2 = time.clock()

print(str(t2-t1)[:5])
