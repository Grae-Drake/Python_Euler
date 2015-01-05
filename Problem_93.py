from __future__ import division

import time
import itertools


t1 = time.clock()


digit_sets = list(itertools.combinations(range(1, 10), 4))


# These are the operator functions we'll apply to the digit sets.
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


# Collect the operator functions together.
functions = [add_digits, subtract_digits, multiply_digits, divide_digits]


def targets(digit_sets):

    # This function accepts a list of digit sets, each of length n,
    # combines each permutation of two digits with each operator function, and
    # returns a list of digit sets of length n-1.
    # We'll want to recursively call this function 3 times on digit_sets.
    results = []
    for digit_set in digit_sets:
        to_combine = list(itertools.combinations(digit_set, 2))
        for digits in to_combine:

            # Grab the remainders
            remainders = list(digit_set)
            for digit in digits:
                remainders.remove(digit)

            # Apply functions and store new sets in results
            for function in functions:
                if function(digits):
                    result = sorted([function(digits)] + remainders)
                    results.append(tuple(result))

    return sorted(list(set(results)))

# Populate a dictionary of digit sets with corresponding target lists
digit_set_targets = {}

for digit_set in digit_sets:
    answer = [x[0] for x in targets(targets(targets([digit_set])))]
    digit_set_targets[digit_set] = answer


# Iterate through digit_set_targets and pull out the digit set with the largest
# number of consecutive targets.
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
