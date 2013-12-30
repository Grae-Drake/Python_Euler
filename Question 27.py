        # Problem 27: Quadratic Primes
def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def consecQuadPrimes(a,b):
    n = 0
    primecount = 0
    finished = False
    while finished == False:
        testnum = n**2 + a*n +b
        if isPrime(testnum) == True:
            n += 1
            primecount += 1
        else:
            finshed = True
            return primecount

alpha = -999
results = []
while alpha < 1000:
        beta = -999
        while beta < 1000:
                results.append([consecQuadPrimes(alpha,beta),alpha,beta])
                beta += 1
        alpha += 1

results.sort()
print(results[-1])
