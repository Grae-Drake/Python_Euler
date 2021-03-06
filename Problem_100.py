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

# Why does the sequence of red and blue numbers increase in proportion to about
# 5.8?!?  I have no idea!


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

    numerator = int(get_numerator(start_number))
    result = None

    while result is not True:
        numerator += 1
        result = is_double(numerator)

    denominator = int(get_denominator(numerator))

    return {
        "blue": numerator,
        "red": denominator - numerator,
        "total": denominator
    }


def main(limit):

    ratio = None
    counter = 21
    results = [{"blue": 15, "red": 7, "total": 21}]
    while results[-1]["total"] < limit:
        results.append(next_arranged_probability(counter))
        ratio = float(results[-1]["total"]) / float(results[-2]["total"])
        counter = results[-1]["total"] * ratio

    return results


if __name__ == "__main__":
    t1 = time.clock()
    print main(1000000000000)[-1]["blue"]
    print "Execution time: {} seconds".format(time.clock() - t1)
