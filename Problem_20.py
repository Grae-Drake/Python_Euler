# Problem 20: Factorial digit sum

def factorial(n):

    # Returns n! (n factorial).
    return n if n <= 1 else n * factorial(n-1)

def sumDigits(n):

    # Returns the sum of the digits of n.
    return sum([int(x) for x in list(str(n))])

def factorialDigitSum(n):
    
    # Returns the sum of the digits of n! (n factorial).
    return sumDigits(factorial(n))

print(factorialDigitSum(100))

