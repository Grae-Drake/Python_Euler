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

def get_cycle(n, lookup, seen):
	# If a new cycle is detected it returns a list of cycle elements.
	# Returns False if the proper factor sum chain is outside lookup or ends
	# without repeating.  Also returns False if the next sum in the chain has
	# already been seen.

	cycle_list = [n]
	cycle_set = set([n])
	next = lookup[n]
	while True:
		if next == 1 or next not in lookup or next in seen:
			return False
		if next in cycle_set:
			return set(cycle_list[cycle_list.index(next):])
		else:
			cycle_set.add(next)
			cycle_list.append(next)
			next = lookup[next]





def main(limit):
	lookup = make_lookup(limit)
	seen = set([1])
	result = {"length": None, "smallest": None}
	for x in xrange(limit):
		new_cycle = get_cycle(x, lookup, seen)
		if new_cycle:
			seen = seen.union()
			if len(new_cycle) > result["length"]:
				result["length"] = len(new_cycle)
				result["smallest"] = min(new_cycle)
	return result




if __name__ == '__main__':
	t1 = time.clock()
	testing = main(limit)
	print testing
	print "Execution time: {} seconds".format(time.clock() - t1)

