    #Problem 63: Powerful digit counts

import time

t1 = time.clock()

count = 0
for x in range(1,10):
    power = 1
    while True:
        if len(str(x ** power)) == power:
            count += 1
        elif len(str(x ** power)) < power:
            break
        power += 1

print(count)
    
t2 = time.clock()

print("Execution time: ", t2-t1)


