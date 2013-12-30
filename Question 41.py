        # Problem 41: Pandigital Primes

"""
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1
    to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
"""
    # Note: answer must be 7 digits or less, as all 8 and 9 digit pandigitals
    # are divisible by 3.
import time
t1 = time.clock()
f = open("1-7_pandigitals.txt")

bigstring = f.read()

f.close()

biglist = bigstring.split()
biglist = [int(x) for x in biglist]
biglist = reversed(biglist)

def isPrime(n):
    if n%2 == 0: return False
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

found = False
answer = []
while found == False:
    for item in biglist:
        if isPrime(item) == True:
            answer.append(item)
            found = True

print(answer)
