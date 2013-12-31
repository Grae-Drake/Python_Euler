# Problem 7: 10001st prime
import sys
sys.path.append("/Users/graedrake/Documents/Projects/Python_Euler/Functions")

import Euler

def main(n):

	# Returns the nth prime number.
	counter = 0
	testnum = 1
	while counter < n:
		testnum = Euler.nextPrime(testnum)
		counter += 1
	return testnum

print(main(10001))