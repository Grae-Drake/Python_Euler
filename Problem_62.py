    #Problem 62: Cubic permutations

import time

t1 = time.clock()

def list_cubes(x):
    # Returns a list of all cube numbers with x digits
    
    output = []
    counter = 1
    while True:
        if counter**3 > 10 ** (x-1):
            output.append(counter**3)
            counter += 1
        else:
            counter += 1
        if counter**3 > 10 ** x:
            break
    return output

def arrange(x):
    if type(x) != int:
        raise ValueError("Argument was not an integer!")
    return "".join(sorted([y for y in str(x)]))

digits = 4
answer = 0
found = False
while found == False:
    permutations = 1
    candidates = list(list_cubes(digits))
    for x in candidates:
        count = 1 
        hashed = arrange(x)
        for y in candidates:
            if y > x:
                if hashed == arrange(y):
                    count += 1
        if count > permutations:
            permutations = count
        if count > 4:
            answer = x
            found = True
            break

    print(digits, " digit squares have only ", count, " permutations.")
    digits += 1

print("The answer is: ", answer)


t2 = time.clock()

print("Execution time: ", t2-t1)


