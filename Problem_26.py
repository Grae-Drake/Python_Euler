    # Problem 26: Reciprical cycles

import time

for x in range(1,11):
    num = 1
    denom = x
    remainder = 0
    expansion = []
    while True:
        expansion.append(num//denom)
        remainder = num % denom
        break
    print(expansion)
    print(remainder)

t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
