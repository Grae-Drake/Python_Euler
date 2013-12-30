    # Problem 69: Prime pair sets
    
    # Find the lowest sum for a set of five primes for which any
    # two primes concatenate to produce another prime.

    # First group is [3, 7, 109, 673]
    # Other groups: [7, 19, 97, 3727], [11, 23, 743, 1871], [13, 19, 577, 28219],
    # [17, 83, 449, 362897]

import time
import Euler

t1 = time.clock()

start_prime = 673
prime_table = {3: False, 5: False, 7: [(2, [3,7])]}

def is_pair(x,y):
    # Returns True if xy and yx are each prime, else returns False
    
    test1 = int(str(x) + str(y))
    test2 = int(str(y) + str(x))
    return Euler.isPrime(test1) == True and Euler.isPrime(test2) == True        
    
def evaluate_prime(prime):
    # Evaluates a prime number and adds a key: value pair to prime_table
    # with a list containing each set of pairs for that prime organized by
    # number of pairs

    candidate = Euler.previous_prime(prime)
    answer = []                                 # This will be the value we return
    finished = False
    pairs = [prime]
    while finished == False:
        while candidate > 2:
            if is_pair(prime, candidate) == True:
                pairs.append(candidate)
            candidate -= 2
        if len(pairs) > 1:
            answer.append((len(pairs), pairs))
            candidate = Euler.previous_prime(pairs[-1])
            pairs = pairs[:-1]
        if len(pairs) < 2:
            finished = True
    if len(answer) == 0:
        prime_table[prime] = False
    else:
        prime_table[prime] = answer

for x in range(8, 700):
    if Euler.isPrime(x) == True:
        evaluate_prime(x)
print(prime_table[13])
    
        
            
        
            

t2 = time.clock()

print(str(t2-t1)[:5])

    
    
    
