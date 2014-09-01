# Problem 95: Amicable chains

import math, time

chains = {}

lookup = {}

def calc_proper_factors(n):
	# Returns a list of proper factors of n
	proper_factors = [[y, n/y] for y in range(2,int(math.sqrt(n) + 1)) if n % y == 0]
	proper_factors = sum(proper_factors, [])
	proper_factors.append(1)
	return set(proper_factors)

def main(limit):
	return calc_proper_factors(limit)

if __name__ == '__main__':
	t1 = time.clock()
	limit = 1000
	for x in range(1,limit):
		chains[x] = main(x)
	print "Execution time: {} seconds".format(time.clock() - t1)

