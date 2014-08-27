# Problem 92: Square digit chains
# Running just under a minute.  Phew.

import time

def next_square_digit(n):

	""" Given n, returns the sum of the squares of the digits of n. """

	digits = [int(x) for x in str(n)]
	total = 0
	for digit in digits:
		total += digit ** 2
	return total

def main(limit):

	""" Returns the count of starting numbers below limit for which the square
	    digit chains converge to 89. """

	# The sum of the squares of the digits of each number below 10,000,000 will
	# always be 567 (the sum of squares of 9,999,999) or lower.  Hence, a dict
	# with keys for each number from 1 to 567 indicating whether the number
	# converges to 1 or to 89 will allow for very fast lookups.

	largest_square_digit = next_square_digit(limit - 1)
	my_dict = {}

	for integer in xrange(1,largest_square_digit + 1):
		tracker = next_square_digit(integer)
		while tracker != 1 and tracker != 89:
			tracker = next_square_digit(tracker)
		my_dict[integer] = tracker
	
	# Loop through numbers below digit and look up whether they converge to 89.
	
	counter = 0

	for number in xrange(1, largest_square_digit + 1):
		if my_dict[number] == 89:
			counter += 1
	for number in xrange(largest_square_digit + 1, limit):
		if my_dict[next_square_digit(number)] == 89:
			counter += 1
	return counter

if __name__ == '__main__':
	t1 = time.clock()
	print(main(10000000))
	print "Execution time: {} seconds".format(time.clock() - t1)