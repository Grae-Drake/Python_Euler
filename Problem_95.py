# Problem 95: Amicable chains

import time

limit = 1000000

chains = {}

lookup = {}

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


def main(limit):
	print len(sieve_proper_factors(limit))


if __name__ == '__main__':
	t1 = time.clock()
	main(limit)
	print "Execution time: {} seconds".format(time.clock() - t1)

