import math

candidates = []

range1 = []
range2 = []

for i in range(1,1000):
        range1.append(i)
        range2.append(i)

for x in range1:
        for y in range2:
                c = math.sqrt(x**2 + y**2)
                if (c%1 == 0) and (x+y+c) == 1000:
                        insert = (c,x,y)
                        candidates.append(insert)

print(candidates)
