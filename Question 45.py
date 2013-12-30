        # Problem 45: Triangular, Pentagonal, and Hexagonal
import math

def pentagon(x):                    # Returns True if the argument is a pentagonal
    y = (math.sqrt(24*x+1)+1)/6
    if y.is_integer():
        return True
    else:
        return False

def triangle(x):                    # Returns True if the argument is triangular
    y = (math.sqrt(8*x +1)-1)/2
    if y.is_integer():
        return True
    else:
        return False
    
counter = 144
answer = 0
found = False

while found == False:
    testnum = counter*(2*counter-1)
    if pentagon(testnum) == True:
        if triangle(testnum) == True:
            answer = testnum
            found = True
    counter += 1

print(answer)
