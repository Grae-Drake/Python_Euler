        # Problem 35: Circular Primes
        
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
    
primeList = primeSieve(100)

print(primeList)


#Mylist = [x for x in map(list, enumerate(array, start = 2))]




