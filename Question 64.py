    #Problem 64: Odd period square roots

import time
import math

t1 = time.clock()

counter = 0
mydict = {}
for x in range(10001):
    if math.sqrt(x) % 1 == 0:
        pass
    else:
        m = 0
        d = 1
        a0 = math.floor(math.sqrt(x))
        a = a0
        sequence = []
        variables = []
        variables.append([m,d,a])
        while True:
            mz = d*a - m
            dz = (x - (mz ** 2))/d
            az = math.floor((a0 + mz)/dz)
            if [mz, dz, az] in variables:
                break
            sequence.append(az)
            variables.append([mz, dz, az])
            m = mz
            d = dz
            a = az
        #mydict[x] = sequence
        if len(sequence) % 2 == 1:
            counter += 1
        
print(counter)
    
t2 = time.clock()

print("Execution time: ", t2-t1)


