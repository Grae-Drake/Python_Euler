# Problem 87: Prime Power Triples

import sys, time
sys.path.append("/Users/graedrake/Documents/Projects/Python_Euler/Functions")

import  Euler

t0 = time.clock()

def main(limit):

	# Returns the number of unique numbers below limit that are the sum of a
	# prime square, prime cube, and prime fourth power.
	fourth_powers = [x ** 4 for x in Euler.prime_sieve(int(limit ** (1/4.0) + 1))]
	third_powers = [x ** 3 for x in Euler.prime_sieve(int(limit ** (1/3.0) + 1))]
	second_powers = [x ** 2 for x in Euler.prime_sieve(int(limit ** (1/2.0) + 1))]
	result = []
	for x in fourth_powers:
		for y in third_powers:
			for z in second_powers:
				if x+y+z < limit:
					result.append(x+y+z)
	return len(set(result))

print main(50000000)
print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."
