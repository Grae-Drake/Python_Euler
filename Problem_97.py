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


def main():

    base = 28433
    exponent = 7830457
    ten_billion = 10 ** 10

    binary_string = "1" + ("0" * (exponent))
    binary_remainder = (int(binary_string, base=2) % ten_billion)

    answer = (binary_remainder * base + 1) % ten_billion
    return answer


if __name__ == "__main__":

    t1 = time.clock()
    print main()
    print time.clock() - t1
