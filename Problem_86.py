# Problem 86: Cuboid route

# For cuboid a,b,c, where a <= b <= c, the shortest route ie equal to
# sqrt((a+b)^2 + c^2).  Thus, the shortest route is an integer when 
# (a+b)^2 + c^2 is a perfect square.  When checking whether a number is a
# perfect square, we can scan a dictionary containing only perfect squares.
# We can reduce the size of the dictionary by placing upper and lower limits
# on the size of square number we're checking against.

# Shortest path squared will be m^2 + 2^2.  M=100: 10004
# Longest path squared will be m^2 + 2m^2.  M=100: 4000000

import math
import time
t0 = time.clock()

m = 1
result = 0
while result < 1000000:
	squares = [x**2 for x in range(m, (3*m)+1)]
	n = 2
	while n <= 2*m:
		hypSquare = m**2 + n**2
		if int(hypSquare) in squares:
			result += math.floor(n/2)
			if n > m:
				result -= n-m -1
		n +=1
	m += 1

print result, m-1
print "Execution time: " + str(time.clock()-t0)[:5] + " seconds."
