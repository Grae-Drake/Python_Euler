# Problem 9: Special Pythagorean triplet

import math

def main(n):
	for a in range(1, n):
		for b in range(1, n):
			c = math.sqrt((a ** 2) + (b ** 2))
			if c % 1 == 0 and (a + b + c) == n:
				print [a,b,c]
				return (a * b * c)
	return "There is no Pythagorean triplet for which a + b + c = " + str(n) + "."

print(main(1000))

# import math

# candidates = []

# range1 = []
# range2 = []

# for i in range(1,1000):
#         range1.append(i)
#         range2.append(i)

# for x in range1:
#         for y in range2:
#                 c = math.sqrt(x**2 + y**2)
#                 if (c%1 == 0) and (x+y+c) == 1000:
#                         insert = (c,x,y)
#                         candidates.append(insert)

# print(candidates)
