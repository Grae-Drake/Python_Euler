# Problem 88: Product-sum numbers

import  Euler, time, operator

t0 = time.clock()

def get_start_set(n):
	"""For a given n, returns a list of numbers of length n. The first element
	is equal to n, the second element is 2, and all remaining elements are 1's.
	"""

	return [n, 2] + [1 for x in range(n-2)]

def sum_equals_product(set):
	"""Returns True if the sum of the elements in set equals the product of the
	elements in set."""

	def prod(iterable):
		return reduce(operator.mul, iterable, 1)

	if sum(set) == prod(set):
		return True
	else:
		return False

for x in range(2,13):
	print get_start_set(x)
	


print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."


