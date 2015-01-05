from __future__ import division

import time
import itertools

t1 = time.clock()

digit_sets = list(itertools.combinations(range(1, 10), 4))

test_set = [digit_sets[0]]


def add_digits(numbers):
    return sum(numbers)


def subtract_digits(numbers):
    numbers = list(numbers)
    numbers.sort()
    return numbers[1] - numbers[0]


def multiply_digits(numbers):
    return numbers[0] * numbers[1]


def divide_digits(numbers):
    numbers = list(numbers)
    numbers.sort()
    if numbers[1] % numbers[0] == 0:
        return int(numbers[1] / numbers[0])
    else:
        return False


functions = [add_digits, subtract_digits, multiply_digits, divide_digits]


def targets(digit_sets):
    results = []
    for digit_set in digit_sets:
        combining = list(itertools.combinations(digit_set, 2))
        for digits in combining:

            # Grab the remainders
            remainders = list(digit_set)
            for digit in digits:
                remainders.remove(digit)
            # remainders = tuple(remainders)

            # Apply functions and store new sets in results
            for function in functions:
                if function(digits):
                    result = sorted([function(digits)] + remainders)
                    results.append(tuple(result))
    return sorted(list(set(results)))

digit_set_targets = {}

for digit_set in digit_sets:
    answer = [x[0] for x in targets(targets(targets([digit_set])))]
    digit_set_targets[digit_set] = answer

stash = [[], 0]
for x in digit_set_targets:
    targets = digit_set_targets[x]
    counter = 1
    for index, target in enumerate(targets):
        if target + 1 in targets:
            counter += 1
        else:
            if counter > stash[1]:
                stash[1] = counter
                stash[0] = x
            counter = 0

print stash

print "Execution time: {}".format(time.clock() - t1)
