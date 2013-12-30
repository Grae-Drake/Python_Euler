    #Problem 66: Diophantine equation

import time, math

t1 = time.clock()

ds = 0
xs = 2
table = {2: 3}

while len(table) < 10:
    candidate = xs**2 - 1
    D = 2
    while D < candidate:
        if D in table:
            D += 1
        else:
            if math.sqrt(candidate/D) % 1 == 0:
                table[xs] = D
            D += 1
    xs += 1


answer = 0
for key, value in table.items():
    if value > answer:
        answer = value
mylist = sorted([x for x in table.items()])

print(mylist)
    

squares = {}        # Format: 81: [


 
t2 = time.clock()

print("Execution time: ", str(t2-t1)[:5])


