    #Problem 66: Diophantine equation

import time, math

t1 = time.clock()

my_dict = {}

for y in range(62):
    if math.sqrt(y)%1 == 0:
        pass
    else:
        counter = 1
        while True:
            x = math.sqrt((y * (counter**2)) + 1)
            # if  x.is_integer() == True:
            if x % 1 == 0:
                my_dict[y] = int(x)
                break
            
            else:
                counter += 1    

answer = 0
D = 0
for y, x in my_dict.items():
    if x > answer:
        answer = x
        D = y

print(D, answer) 
t2 = time.clock()

print("Execution time: ", t2-t1)


