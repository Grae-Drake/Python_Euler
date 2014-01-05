# Problem 12: Highly divisible Triangular number

def calcFactors(n):

    # Returns a the number of factors of n
    factors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return len(set(factors))

def main(n):
    
    # Returns the first triangular number with at least n factors
    triangle = 1
    counter = 2
    while True:
        if calcFactors(triangle) >= n:
            return triangle
        else:
            triangle += counter
            counter += 1

print(main(500))
        
