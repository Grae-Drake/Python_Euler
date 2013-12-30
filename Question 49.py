        # Problem 49: Prime permutations

import time
t1 = time.clock()

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

primes = []                 # Creat a list of our candidate primes
for x in range(1000,10000):
    if isPrime(x) == True:
        primes.append(x)

mydict = {}                 # Create a dictionary of primes and thier sorted digits
for prime in primes:
    digits = "".join(sorted(str(prime)))
    mydict[str(prime)] = digits

from collections import Counter # Create a list of the sorted digits that are unique
c = Counter(mydict.values())
unique_hashes = []
for key, value in c.items():
    if value > 2:
        unique_hashes.append(key)

shortlist = []                  # Get rid of the digits with only 1 or 2 instances
for key, value in mydict.items():
    if value in unique_hashes:
        shortlist.append(value)
        shortlist.append(key)

pairs = zip(shortlist[::2], shortlist[1::2])    # create a dictionary of digits: [prime1, prime2]
usefuldict = {}
for x in pairs:
    usefuldict.setdefault(x[0], []).append(x[1])

answer = []
for index, candidates in usefuldict.items():    # Go through the new dict for arithmet sequences
    candidates = sorted(candidates)
    differences = []                            
    for xindex, x in enumerate(candidates):
        for yindex, y in enumerate(candidates):
            if yindex > xindex:
                if str(int(y) + (int(y)-int(x))) in candidates:
                    print(x)
                    print(y)
                    print(int(y) + (int(y)-int(x))) 

t2 = time.clock()
print(t2 - t1)
                
"""for item in differences:
        if differences.count(item) == 2:
            answer = candidates
            print(item)

for xindex, x in enumerate(answer):
        for yindex, y in enumerate(answer):
            if yindex > xindex:
                print(x + " minus " + y + ": " + str(int(y)-int(x)))"""

            
        




#{hash1: [prime1, prime2, prime3], hash2: [prime4, prime5, prime6]}
#print(sum(1 for value in c.values()if value == 2))
#for key, value in mydict.items():
#    frequency = sum(1 for x in mydict.values() if x == value)
#    print(str(value) + ": " + str(frequency))
