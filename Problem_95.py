# Problem 95: Amicable chains

import time

limit = 1000000

def sieve_proper_factors(limit):
	# Returns a dictionary with keys from 1 to limit with corresponding sets
	# containing each key's proper factors

	numbers = [set([1]) for x in xrange(limit)]
	start_index = 2
	for x in xrange(start_index, limit):
		multiplier = 2
		while multiplier * x < limit:
			numbers[multiplier * x].add(x)
			multiplier += 1
	return numbers

def make_lookup(limit):
	# Returns a dictionary; keys are integers, values are sum of proper factors
	lookup = {}
	for number, factors in enumerate(sieve_proper_factors(limit)):
		lookup[number] = sum(factors)
	return lookup

def main(limit):
	return make_lookup(limit)


if __name__ == '__main__':
	t1 = time.clock()
	testing = main(limit)
	print "Execution time: {} seconds".format(time.clock() - t1)

