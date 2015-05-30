# Problem 101: Optimum polynomial

# This is the generating function, as given by the problem description.


def generating_function(n):

    exponents = range(11)

    coefficients = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

    polynomial = [coefficients[x] * (n ** exponents[x]) for x in range(11)]

    return sum(polynomial)


# Ok, now, how do we generate a BOP (Bad Optimum Polynomial)?
# Let's talk about the terms of generating_function as t1, t2, t3, etc.
# They are: [1, 683, 44287, 838861, 8138021, 51828151, 247165843, 954437177,
#            3138105961, 9090909091, ...]
# BOP1 is: y = 1
# BOP2 is: ((n * (t2 - 1)) - (t2 - 2))


# Work goes here.


if __name__ == '__main__':
    for x in xrange(1, 11):
        print generating_function(x)
