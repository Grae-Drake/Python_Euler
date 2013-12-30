    # Problem 69: totient maximum

import time, Euler
t1 = time.clock()
answer = 1
n = 0
for x in range(2, 10001):
    rp_counter = 1
    for y in range(2,x):
        if Euler.highest_common_factor(x,y) == 1:
            rp_counter += 1
    ratio = x/rp_counter
    if ratio > answer:
        answer = ratio
        n = x

print(n, " has the largest ratio: ", answer)
            
t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
