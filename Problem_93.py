from __future__ import division

import time
import itertools

t1 = time.clock()

limit = 20
digits = range(1, 10)
field = range(1, limit)

# Build dictionaries allowing us to decompose a number into it's subtraction,
# addition, division, and multiplication factors.

sub_factors = {}
add_factors = {}
div_factors = {}
mult_factors = {}

for x in field:
    for y in xrange(x, limit):

        # Populate sub_factors dictionary
        sub = y - x
        if sub not in sub_factors:
            sub_factors[sub] = []
        sub_factors[sub].append(tuple(sorted([x, y])))

        # Populate add_factors dictionary
        add = y + x
        if add not in add_factors:
            add_factors[add] = []
        add_factors[add].append(tuple(sorted([x, y])))

        # Populate mult_factors dictionary
        mult = y * x
        if mult not in mult_factors:
            mult_factors[mult] = []
        mult_factors[mult].append(tuple(sorted([x, y])))

        # Populate div_factors dictionary
        if y % x == 0:
            div = y / x
            if div not in div_factors:
                div_factors[div] = []
            div_factors[div].append(tuple(sorted([x, y])))


# Ok, we've built the decomposition dicts, time to start using them!
# More to come here.

def decompositions_count(n):

    # This returns the total number of sub, add, mult and div factors for n.
    # Helpful for tinkering.
    total = 0
    if n in sub_factors:
        total += len(sub_factors[n])
    if n in add_factors:
        total += len(add_factors[n])
    if n in mult_factors:
        total += len(mult_factors[n])
    if n in div_factors:
        total += len(div_factors[n])

    return total


def decompose_number(n):

    # Returns the set of all possible - + * / factors of n.
    result = []
    if n in sub_factors:
        result += sub_factors[n]
    if n in add_factors:
        result += add_factors[n]
    if n in mult_factors:
        result += mult_factors[n]
    if n in div_factors:
        result += div_factors[n]
    return set(result)


testing = 1


def decompose_set(digit_sets):

    # Takes an input set of tuples, decomposes each tuple, and
    # returns a new set of all possible decompositions.
    result = []
    for digit_set in digit_sets:
        digit_set = list(digit_set)
        for digit in digit_set:
            decompositions = decompose_number(digit)
            remainder = list(digit_set)
            remainder.remove(digit)
            for decomposition in decompositions:

                # This is a tuple we may return.
                candidate = tuple(sorted(list(decomposition) + remainder))

                # Check to see if tuple elements are too big.
                if len("".join([str(x) for x in candidate])) > 4:
                    continue

                # Check to see if the final tuples have duplicates
                if len(candidate) == 4 and len(set(candidate)) != 4:
                    continue

                result.append(candidate)
    return set(result)

answer = decompose_set(decompose_set(decompose_number(1)))
for x in list(itertools.combinations(range(1, 10), 4)):
    if x not in answer:
        print "{} is not in answer".format(x)
print len(answer)

# for index, number in enumerate(testing):
#     result = []
#     result += decompose_number(number)

# for x in testing:
#     print x

print time.clock() - t1
