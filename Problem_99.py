"""
    Project Euler Problem 99: Largest Exponential.
    https://projecteuler.net/problem=99
"""

import time
import math


def get_numbers(input_file):

    with open(input_file) as number_file:
        number_list = [x.rstrip().split(',') for x in number_file.readlines()]
        number_list = [(int(x[0]), int(x[1])) for x in number_list]
    return number_list


def bigger_number(n1, n2):

    """
        Compares n1 and n2, returning the larger number.  Both n1 and n2 must
        be formatted as a tuple (x, y) where x is the base and y is the
        exponent.  For example: 1234 ** 5678 would be (1234, 5678).
    """

    if n1[1] * math.log(n1[0]) > n2[1] * math.log(n2[0]):
        return n1
    else:
        return n2


def main(input_file):

    number_list = get_numbers(input_file)

    biggest = number_list[0]

    for number in number_list[1:]:
        biggest = bigger_number(biggest, number)

    return (number_list.index(biggest), biggest)


if __name__ == "__main__":

    t1 = time.clock()

    input_file = "TextFiles/p099_base_exp.txt"

    print "The answer is {}.".format(main(input_file))

    print "Execution time: {}".format(time.clock() - t1)
