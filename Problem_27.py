        # Problem 27: Quadratic Primes
def is_prime(n):

    # Returns True is n is prime, otherwise False
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

    # Given parameters a and b, returns the number of consecute prime numbers
    # resulting from the quadratic formula n**2 + an + b, starting from n = 0.
    n = 0
    primecount = 0
    while True:
        if is_prime(n**2 + a*n +b):
            n += 1
            primecount += 1
        else:
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
