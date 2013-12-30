        # Problem 52: Permuted multiples

import time
t1 = time.clock()

def compare (x,y):
    # Returns True if x is a permutation of y
    string1 = "".join(sorted([i for i in str(x)]))
    string2 = "".join(sorted([j for j in str(y)]))
    if string1 == string2:
        return True
    else:
        return False

reference = 1000
counter = reference
answer = 0
while answer == 0:
    if compare(counter, counter*2) == True:
        if compare(counter, counter*3) == True:
            if compare(counter, counter*4) == True:
                if compare(counter, counter*5) == True:
                    if compare(counter, counter*6) == True:
                        answer = counter
    counter += 1
    if counter/reference > (10/6):
        reference *= 10
        counter = reference

print(str(answer) + " is the answer ")
print("The multiples are: " + str(list(answer*x for x in range(1,7))))
t2 = time.clock()
print("Time = " + str(t2-t1)[:4] + " seconds.")
