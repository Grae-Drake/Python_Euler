        # Problem 58: Spiral primes

import time
import math
import Euler
t1 = time.clock()

found = False
array = [[1, 0, 0]]
corners = []
counter = 1
composite_count = 0
prime_count = 0

while found == False:  # Change to: while found == False
    counter += 2
    corner1 = False
    corner2 = False
    corner3 = False
    xstart = counter//2
    ystart = (xstart * -1) + 1
    x = xstart
    y = ystart
    for j in range((counter * 4)- 4):
        new_entry = [array[-1][0] + 1, x, y]
        array.append(new_entry)
        if abs(x) == abs(y):
            corners.append(new_entry)
        if corner3 == True:
            x += 1
        elif corner2 == True:
            y -= 1
        elif corner1 == True:
            x -= 1
        else:
            y += 1
        if x == xstart:
            if y == xstart:
                corner1 = True
        if x == xstart * -1:
            if y == xstart:
                corner2 = True
        if x == (xstart * -1):
            if y == (xstart * -1):
                corner3 = True
                
    for item in corners:
        if Euler.isPrime(item[0]) == True:
            prime_count += 1
        else:
            composite_count += 1
    ratio = prime_count / (prime_count + composite_count + 1)
    if ratio < 1/10:
        found = True

t2 = time.clock()

print(counter)
print("Execution time: " + str(t2-t1)[:5])

