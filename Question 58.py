        # Problem 58: Spiral primes

import time
import Euler

t1 = time.clock()

diagonal = 1
primes = []
non_primes = [1]
side_length = 3
ratio = 1

while ratio > 1/10:        # Change to: while found = False
    for x in range(4):
        diagonal += side_length - 1
        if Euler.isPrime(diagonal) == True:
            primes.append(diagonal)
        else:
            non_primes.append(diagonal)
    ratio = len(primes) / (len(primes) + len(non_primes))
    side_length += 2

t2 = time.clock()

print("Side length = ", side_length - 2)
print(str(t2-t1)[:9])
