# Problem 92: Square digit chains

import time

# Sets to contain numbers converging to 1 and to 89.
# Using sets because hashable
ones = set([1])
eighty_nines = set([89])

limit = 10000000

def next_square_digit(n):

	""" Given n, returns the sum of the squares of the digits of n. """

	digits = [int(x) for x in str(n)]
	total = 0
	for digit in digits:
		total += digit ** 2
	return total

def main():
	counter = 0
	for number in range(1, limit):
		trail = [number]
		while trail[-1] not in ones and trail[-1] not in eighty_nines:
			trail.append(next_square_digit(trail[-1]))
		if trail[-1] in ones:
			for x in trail[:-1]:
				ones.add(x)
		elif trail[-1] in eighty_nines:
			for x in trail[:-1]:
				eighty_nines.add(x)
			counter += 1
		else:
			print "Fuck me, this isn't supposed to print"
	return counter





if __name__ == '__main__':
	t1 = time.clock()
	print(main())
	print "Execution time: {} seconds".format(time.clock() - t1)