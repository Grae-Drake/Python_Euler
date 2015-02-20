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
    # n1 = (num / denom)
    # n2 = (num - 1 / denom - 1)
    # product = n1 * n2

# We can determine num for a given denom:
    # num = ceil(denom * (2 ** .5) / 2)

# We can also determine denom for a given num:
    # denom = floor(num / ((2 ** .5) / 2))

# Starting with denom = 10^12, we calculate the first num, incrementing num by
# 1 and testing whether the resulting product == .5.
