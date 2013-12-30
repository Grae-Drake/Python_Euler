        # Problem 376: Truncatable Primes

""" The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from
    left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def primeSieve(limit):
    import time
    t1 = time.clock()
    array = [[x,True] for x in range(2,limit)]

    for x in array:
        value = x[0]
        primeness = x[1]
        for y in range((value)*2, limit, value):
            array[y-2][1] = False
    t2 = time.clock()
    print("Sieve time: " + str(t2 - t1))
    results = []
    for item in array:
        if item[1] == True:
            results.append(item[0])
    t3 = time.clock()
    print("List time: " + str(t3 - t2))
    return results

def isPrime(n):
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

def truncatePrimes(limit):
    # Tests each prime less than limit for truncatableness.
    # Returns a list of all such primes.
    
    startPrimes = primeSieve(limit)
    answers = []
    for prime in startPrimes:
        truncatable = True
        temp = str(prime)
        
        for x in range(len(str(prime))-1):  # Test forwards
            temp = temp[1:]
            if isPrime(int(temp)) != True:
                truncatable = False
                                            
        temp = str(prime)                   # Test backwards
        for x in range(len(str(prime))-1): 
            temp = temp[:-1]
            if isPrime(int(temp)) != True:
                truncatable = False
                
        if truncatable == True:
            answers.append(prime)
    return answers
                
            


print(sum(truncatePrimes(1000000))-17)


