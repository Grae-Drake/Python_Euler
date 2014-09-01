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

def get_cycle(lookup, n):
	# Returns False if the proper factor sum chain is outside lookup or ends
	# without repeating.  If a cycle is detected it returns a list of cycle
	# elements.

	# Could refactor to prevent duplicate positives

	cycle_list = [n]
	cycle_set = set([n])
	next = lookup[n]
	while True:
		print next
		if next == 1 or next not in lookup:
			return False
		if next in cycle_set:
			return cycle_list[cycle_list.index(next):]
		else:
			cycle_set.add(next)
			cycle_list.append(next)
			next = lookup[next]





def main(limit):
	print get_cycle(make_lookup(16000), 12496)


if __name__ == '__main__':
	t1 = time.clock()
	testing = main(limit)
	print "Execution time: {} seconds".format(time.clock() - t1)

