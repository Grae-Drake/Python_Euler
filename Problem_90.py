# Problem 90: Cube digit pairs

import time, itertools

answer = []

def main():
	squares = [[0,1], [0,4], [0,9], [1,6], [3,6], [4,9], [6,4], [8,1]]

	lefts = itertools.combinations(range(10), 6)
	count = 0
	left_count = 0
	right_count = 0
	for left in lefts:
		left_count += 1
		rights = itertools.combinations(range(10), 6)
		for right in rights:
			right_count += 1
			if (0 in left and 1 in right) or (1 in left and 0 in right):
				pass
			else:
				continue
			if (0 in left and 4 in right) or (4 in left and 0 in right):
				pass
			else:
				continue
			if (2 in left and 5 in right) or (5 in left and 2 in right):
				pass
			else:
				continue
			if (8 in left and 1 in right) or (8 in left and 1 in right):
				pass
			else:
				continue
			if (0 in left and (6 in right or 9 in right)) or (0 in right and (6 in left or 9 in left)):
				pass
			else:
				continue
			if (1 in left and (6 in right or 9 in right)) or (1 in right and (6 in left or 9 in left)):
				pass
			else:
				continue
			if (3 in left and (6 in right or 9 in right)) or (3 in right and (6 in left or 9 in left)):
				pass
			else:
				continue
			if (4 in left and (6 in right or 9 in right)) or (4 in right and (6 in left or 9 in left)):
				pass
			else:
				continue
			if (left, right) not in answer and (right, left) not in answer:
				answer.append((left, right))
			print (left, right)
			count += 1


	print "count = {}".format(count)
	print "leftcount = {}".format(left_count)
	print "rightcount = {}".format(right_count)
	print "len answer = {}".format(len(answer))


if __name__ == '__main__':
	t1 = time.clock()
	main()
	print "Execution time: {} seconds".format(time.clock() - t1)
