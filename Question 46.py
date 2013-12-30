        # Problem 46: Goldbach's Other Conjecture
""" This runds too damn long.  Seems like a lot of time is spent
    on sieving.  If we could instead build up a list of primes
    (maybe with nextPrime) we wouldn't have to run a new sieve each time.
"""
        
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

def primeSieve(limit):
    array = [[x,True] for x in range(2,limit)]
    
    for x in array:
        value = x[0]
        primeness = x[1]
        for y in range((value)*2, limit, value):
            array[y-2][1] = False

    results = []
    for item in array:
        if item[1] == True:
            results.append(item[0])

    return results

def goldbach(n):
    # Returns True if the argument is an odd composite number that is
    # the sum of a prime and a twice a square
    primes = primeSieve(n)
    answer = (False, 0)
    for prime in primes:
        counter = 1
        determined = False
        while determined == False:
            testnum = prime + (2*(counter**2))
            if testnum < n:
                counter += 1
            if testnum == n:
                answer = (True, prime, (2*(counter**2)))
                determined = True
            if testnum > n:
                determined = True
    return answer

def main():
    counter = 9
    answer = 0
    found = False
    while found == False:
        if isPrime(counter) == True:
            counter += 2
            print(str(counter) + " is not the answer")
        else:
            if goldbach(counter) == False:
                found = True
                answer = counter
            else:
                counter += 2
    return answer
import time
t1 = time.clock()
for x in range(1000):
    primeSieve(x)

t2 = time.clock()
print(t2-t1)
        










