        # Problem 47: Distinct Prime Factors
""" What are the first four consecutive numbers that each have
    exactly four distinct prime factors?
"""

def factorCount(n, primes):
    # This function returns the number of distinct prime factors
    # that the first argument has.
    
    # For example, the prime factors of 10 are 5 and 2, so
    # factorCount(10) will return 2.  The prime factors of 20 are
    # 2, 2, 5 (or 2**2, 5), so factorCount(20) will also return 2.

    # Note: the second argument must be a list of primes smaller
    # than n.

    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
    return len(set(factors))            

def nextPrime(n):
    # Returns the smallest prime number larger than the argument
    testnum = n + 1
    answer = 0
    found = False
    while found == False:
        if isPrime(testnum) == True:
            answer = testnum
            found = True
        else:
            testnum += 1
    return answer

def isPrime(n):
    # Returns true if the argument is a prime number
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def main():
    primes = []
    counter = 2
    found = False
    factors1 = [0,0]
    factors2 = [0,0]
    factors3 = [0,0]
    factors4 = [0,0]
    while found == False and counter < 1000000:
        if isPrime(counter) == True:
            primes.append(counter)
            counter += 1
        else:
            factors4[0] = factors3[0]
            factors4[1] = factors3[1]
            factors3[0] = factors2[0]
            factors3[1] = factors2[1]
            factors2[0] = factors1[0]
            factors2[1] = factors1[1]
            factors1[0] = counter
            factors1[1] = factorCount(counter, primes)
            counter += 1
        if factors1[1] == 4 and factors2[1] == 4 and factors3[1] == 4 and factors4[1] == 4:
            if factors1[0] - factors4[0] == 3:
                found = True
    print(factors1)
    print(factors2)
    print(factors3)
    print(factors4)

import time
t1 = time.clock()

main()

t2 = time.clock()

print(t2-t1)




            
    
