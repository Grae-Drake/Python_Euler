        # Problem 51: Prime digit replacements
import Euler
import itertools
import time
t1 = time.clock()

def digitCount(argument, character):
    # Returns the number of times character appears in argument
    argument = str(argument)
    character = str(character)
    count = 0
    for x in argument:
        if x == character:
            count += 1
    return count

def replaceDigit(number, digit, replacement):
    # Replaces each instance of digit with replacement and returns
    # the new number.
    number = str(number)
    replacement = str(replacement)
    digit = str(digit)
    newnum = [x if x != digit else replacement for x in number]
    return int("".join(newnum))

def permutePrimes(prime, character):
    # Replaces each instance of character in prime with 0-9 and
    # returns a list of each resulting number that is also prime
    digits = [x for x in range(10)]
    digits = list(filter(lambda x: x != character, digits))
    answers = [prime]
    for x in digits:
        testnum = replaceDigit(prime, character, x)
        if Euler.isPrime(testnum) == True:
            if len(str(testnum)) == len(str(prime)):
                answers.append(testnum)
    return answers

counter = 0
answer = 0
permutations = []
while answer == 0:
    counter = Euler.nextPrime(counter)
    for x in range(10):
        if digitCount(counter,x) > 1:
            if len(permutePrimes(counter, x)) > 7:
                   permutations = permutePrimes(counter, x)
                   answer = permutations[0]
    
print("The answer is " + str(answer))
print("The primes are: " + str(permutations))

t2 = time.clock()
print("Execution time = " + str(t2-t1)[:5] + " seconds")
