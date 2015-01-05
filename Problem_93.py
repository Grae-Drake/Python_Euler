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


def digit_set_targets(digit_sets):

    # Populate a dictionary of digit sets with corresponding target lists
    result = {}
    for digit_set in digit_sets:
        target_list = [x[0] for x in targets(targets(targets([digit_set])))]
        result[digit_set] = target_list
    return result


def most_consecutive_targets():

    # Iterate through digit_set_targets and pull out the digit set with the
    # largest number of consecutive targets.
    result = [[], 0]
    targets_dictionary = digit_set_targets(digit_sets)
    for x in targets_dictionary:
        targets = targets_dictionary[x]
        counter = 1
        for index, target in enumerate(targets):
            if target + 1 in targets:
                counter += 1
            else:
                if counter > result[1]:
                    result[1] = counter
                    result[0] = x
                counter = 0
    return result


def main():
    return most_consecutive_targets()

if __name__ == '__main__':
    print main()
    print "Execution time: {}".format(time.clock() - t1)
