    # Problem 71: Ordered fractions

import time
from fractions import Fraction
t1 = time.clock()

ceiling = [3,7]
candidate = [428571,1000000]
floor = [428571,1000000]
while candidate[1] > 1 and candidate[0] > 1:
    if (candidate[0]/candidate[1]) >= (ceiling[0]/ceiling[1]):
        candidate[0] -= 1
    else:
        if (candidate[0]/candidate[1]) > (floor[0]/floor[1]):
            floor[0] = candidate[0]
            floor[1] = candidate[1]
        candidate[1] -= 1

print(floor)

       
        




t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
