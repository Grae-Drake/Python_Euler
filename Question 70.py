    # Problem 70: Totient permutation
    # candidate: 7026037

import time, Euler, math
t1 = time.clock()

limit = 10000000
root = Euler.previous_prime(int(math.sqrt(limit)))
# 3137 is the largest prime the square of which is < 10,000,000,
# Equivalent to Euler.previous_prime(int(math.sqrt(10000000)))

primes = {0: root}
large_prime_counter = 0
small_prime_counter = 0
composites = {}
large = root
small = root
while small > 2:
    composite = large*small

        # Deal with the case where composite is less than limit
    if composite < limit:
        
        phi = composite - (large + small - 1)

        # Put the composite in the dictionary if it's a permutation
        if (int("".join(sorted([x for x in str(composite)]))) ==
            int("".join(sorted([x for x in str(phi)])))):
            composites[composite] = [large, small, phi]

         # Increase large and add it to primes if necessary   
        large_prime_counter +=1
        if large_prime_counter not in primes:
            primes[large_prime_counter] = Euler.nextPrime(primes[large_prime_counter-1])
        large = primes[large_prime_counter]

        # Deal with the case where composite is too big
    else:
        small_prime_counter -= 1
        large_prime_counter = small_prime_counter +1
        primes[small_prime_counter] = Euler.previous_prime(primes[small_prime_counter+1])
        small = primes[small_prime_counter]
        large = primes[large_prime_counter]

min_ratio = 3
answer = 0
for key, value in composites.items():
    n = key
    phin = value[2]
    ratio = n/phin
    if ratio < min_ratio:
        min_ratio = ratio
        answer = n
        
print(answer)
            
            
t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
