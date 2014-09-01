# Problem 95: Amicable chains

import math, time

limit = 1000000

chains = {}

lookup = {}

def calc_proper_factors(n):
	# Returns a set of proper factors of n
	answer = set([1])
	for x in range(2, int(math.sqrt(n) + 1)):
		if n % x == 0:
			answer.add(x)
			answer.add(x / n)
	return answer

def sum_proper_factors(n):
	# Returns the sum of the proper factors of n
	return sum(calc_proper_factors(n))

def find_chain(n):
	# Returns the elements of the amicable chain starting with n
	trail = set([n])
	checking = sum_proper_factors(n)
	while checking not in trail:
		trail.add(checking)
		checking = sum_proper_factors(checking)
	return trail

def main(limit):
	for x in range(1, limit):
		chains[x] = sum_proper_factors(x)
	# for x,y in chains.items():
	# 	print x, y

if __name__ == '__main__':
	t1 = time.clock()
	main(limit)
	print "Execution time: {} seconds".format(time.clock() - t1)

