        # Problem 35: Circular Primes

import time

def primeSieve(limit):
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

# Now that we have our list of primes and a primality tester,
# let's get down to businees generating circular primes.
tStart = time.clock()
primeList = primeSieve(1000000)
answers = []
for item in primeList:
    circulars = [str(item)]                 # Will contain permutations of each prime
    newnum = circulars[0]                   # String of original prime
    for x in range(len(newnum)-1):          # Create each permutation and add it to circulars
        newnum = newnum[1:] + newnum[0]
        circulars.append(newnum)
    circularityTest = True
    for y in circulars:                     # Test each permutation and add to answers
        if isPrime(int(y)) != True:
            circularityTest = False
    if circularityTest == True:
        answers.append(item)
        
t4 = time.clock()
print("Circularity Test time: " + str(t4-tStart))
print(len(answers))
        




#Mylist = [x for x in map(list, enumerate(array, start = 2))]




