        # Problem 46: Goldbach's Other Conjecture
        
        # Find the smallest odd composite number that cannot be written as
        # the sum of a prime and twice a square.

import time, Euler
t1 = time.clock()

primes = [2,3,5,7,11]
candidate = 9
answer = 0
while True:
    if candidate == primes[-1]:
        primes.append(Euler.nextPrime(candidate))
        candidate += 2
    else:
        answer_found = False
        goldbach = False
        for prime in reversed(primes[:-1]):
            counter = 1
            while goldbach == False:
                result = (prime + (2 * (counter**2)))
                if result == candidate:
                    goldbach = True
                    candidate += 2
                elif result < candidate:
                    counter += 1
                else:
                    break
            if goldbach == True:
                break
        if goldbach == False:
            answer = candidate
            break
                    
t2 = time.clock()

print "The answer is " + str(answer)
print "Execution time: " + str(t2-t1)[:5]
            





