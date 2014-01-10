# Problem 20: Factorial digit sum

def factorial(n):

    # Returns n! (n factorial).
    return n if n <= 1 else n * factorial(n-1)

def sum_digits(n):

    # Returns the sum of the digits of n.
    return sum([int(x) for x in list(str(n))])

def factorial_digit_sum(n):
    
    # Returns the sum of the digits of n! (n factorial).
    return sum_digits(factorial(n))

print(factorial_digit_sum(100))

