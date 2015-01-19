"""
    Projec Euler, Problem 97.

    The first known prime found to exceed one million digits was discovered in
    1999, and is a Mersenne prime of the form (2 ** 6,972,593) - 1;
    it contains exactly 2,098,960 digits.  Subsequently other Mersenne primes,
    of the form (2 ** p) -1 have been found which contain more digits.

    However, in 2004 there was found a massive non-Mersenne prime which
    contains 2,357,207 digits: 28433 * (2 ** 7830457) +1.

    Find the last ten digits of this prime number.

"""

import time


def main(base, exponent, num_digits):

    # Finding large powers of 2 is easy in binary.
    binary_string = "1" + ("0" * (exponent))
    binary_remainder = (int(binary_string, base=2) % (num_digits ** 10))

    answer = (binary_remainder * base + 1) % (num_digits ** 10)
    return answer


if __name__ == "__main__":

    t1 = time.clock()

    # Constants from the problem.
    base = 28433
    exponent = 7830457
    num_digits = 10

    print main(base, exponent, num_digits)

    print time.clock() - t1
