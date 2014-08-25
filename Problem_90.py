# Problem 90: Cube digit pairs

import time, itertools

def main():
	squares = [[0,1], [0,4], [0,9], [1,6], [3,6], [4,9], [6,4], [8,1]]

	lefts = itertools.combinations(range(10), 6)
	count = 0
	for left in lefts:
		if 2 not in left and 5 not in left:
			pass
		else:
			rights = itertools.combinations(range(10), 6)
			for right in rights:
				if 2 not in right and 5 not in right:
					pass
				else:
					for square in squares:
						if square[0] in left and square[1] in right:
							print square
							continue
						elif square[1] in left and square[0] in right:
							print square
							continue
						else:
							break

	print count

if __name__ == '__main__':
	t1 = time.clock()
	main()
	print "Execution time: {} seconds".format(time.clock() - t1)
