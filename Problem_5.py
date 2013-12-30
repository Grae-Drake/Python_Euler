range20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primes = [2,3,5,7,11,13,17,19]

primeFactors = []

counter = 1

for x in primes:
        while any(i%x == 0 for i in range20):
                for i in range20:
                        if i % x == 0:
                                primeFactors.append(x)
                                range20.remove(i)
                                range20.append(i/x)

for i in primeFactors:
        counter *= i

print(primeFactors)

print(range20)

print(counter)

