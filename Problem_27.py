        # Problem 27: Quadratic Primes
import time
t0 = time.clock()

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

def consecutive_quadratic_primes(a,b):

    # Given parameters a and b, returns the number of consecutive prime numbers
    # resulting from the quadratic formula n**2 + an + b, starting from n = 0.
    n = 0
    primecount = 0
    while True:
        if is_prime(n**2 + a*n +b):
            n += 1
            primecount += 1
        else:
            return primecount

def main(limit):
    result = [0,0,0]
    for b in range(-limit + 1, limit):
        if is_prime(abs(b)):
            for a in range(-limit + 1, limit):
                consecutive = consecutive_quadratic_primes(a,b)
                if consecutive > result[0]:
                    result = [consecutive,a,b]
    return result

print main(1000)

print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."
