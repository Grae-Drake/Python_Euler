# Problem 5: Smallest multiple
import sys
sys.path.append("/Users/graedrake/Documents/Projects/Python_Euler/Functions")

import Euler, math

def main(limit):

	# Iterates through each number less than limit testing for primeness.
	# Counter is multiplied by each prime number for the a number of times
	# equal to the greatest number of times that prime divides a number less
	# than or equal to the limit.  For example, 2 divides 8 3 times (8 = 2*2*2),
	# so when limit == 10 counter is multiplied by 2^3.
	counter = 1
	for x in range(2, limit+1):
		if Euler.isPrime(x):
			counter *= (x ** math.floor(math.log(limit, x)))
	return counter

print(main(20))