        # Problem 50: Consecutive Prime Sum
import time
t1 = time.clock()
import Euler
limit = 4000
primes = [x for x in Euler.primeSieve(limit)]
answer = [(0,[])]
for x, prime1 in enumerate(primes):
    startprime = x
    sequence = []
    counter = 0
    for y, prime2 in enumerate(primes):
        if y >= x:
            counter += prime2
            if Euler.isPrime(counter) == True:
                if counter < 1000000:
                    sequentials = [x for x in primes[x:y+1]]
                    if len(answer[0][1]) < len(sequentials):
                        answer[0] = ((counter, sequentials))

print("Prime = " + str(answer[0][0]) + " ; Length of sequence: " + str(len(answer[0][1])))
print("Sequence start = " + str(answer[0][1][0]) + " ; Sequence end = " + str(answer[0][1][-1]))
t2 = time.clock()
print("Runtime = " + str(t2-t1)[:4] + " seconds")
