# Problem 100: Arranged Probability

"""
    If a box contains twenty-one coloured discs, composed of fifteen blue discs
    and six red discs, and two discs were taken at random, it can be seen that
    the probability of taking two blue discs, P(BB) = (15/21) * (14/20) = 1/2.

    The next such arrangement, for which there is exactly 50 percent chance of
    taking two blue discs at random, is a box containing eighty-five blue discs
    and thirty-five red discs.

    By finding the first arrangement to contain over 1,000,000,000,000 discs in
    total, determine the number of blue discs that the box would contain.
"""

# This problem is similar to #94: Almost equilateral triangles.
# (15 / 21) and (14 / 20) each approximate (sqrt(2) / 2).
# The form of this problem is:
#   n1 = (num / denom)
#   n2 = (num - 1 / denom - 1)
#   product = n1 * n2

# We can determine num for a given denom:
#   num = ceil(denom * (2 ** .5) / 2)

# We can also determine denom for a given num:
#   denom = floor(num / ((2 ** .5) / 2))

# Starting with denom = 10^12, we calculate the first num, incrementing num by
# 1 and testing whether the resulting product == .5.

# NOTE 1: This program works, but reaches the time limit near 10^8, while the
# problem requires efficient calculation up to 10^12

# NOTE 2: Is it possible to calculate the next solution directly from the
# previous?  Answers seem to be separated by a factor of ~5.8.  E.g, the first
# several numerators are: [15, 85, 493, 2871, 16731, 97513, 568345, 3312555]


import math
import time


def next_arranged_probability(start_number):

    def get_denominator(numerator):
        return math.floor(numerator / ((2 ** 0.5) / 2))

    def get_numerator(denominator):
        return math.ceil(denominator * (2 ** 0.5) / 2)

    def is_double(numerator):

        denominator = get_denominator(numerator)
        n1 = numerator * (numerator - 1)
        n2 = denominator * (denominator - 1)
        return n2 % n1 == 0

    numerator = get_numerator(start_number)
    result = None

    while result is not True:
        numerator += 1
        result = is_double(numerator)

    return (numerator, get_denominator(numerator), result)


if __name__ == "__main__":
    t1 = time.clock()
    print next_arranged_probability(803761)
    print "Execution time: {} seconds".format(time.clock() - t1)
