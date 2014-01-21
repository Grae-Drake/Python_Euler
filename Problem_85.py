# Problem 85: Counting rectangles

def count_rectangles(x,y):

	# Returns the number of component rectangles in a rectangular x by y grid.
	return x * (x+1) * y * (y+1) / 4

def bracket_target(limit, height):

	# Returns a tuple containing the largest count_rectangles(height, x) less
	# than limit and the smallest count_rectangles(height, x) greater than limit.

	testnum = 0
	x = 1
	while testnum < limit:
		testnum = count_rectangles(height, x)
		x += 1
	return (count_rectangles(height, x-1), count_rectangles(height, x-2))




def main(limit):

	# Finds the x by y grid with component rectangles closest to limit.
	# Starts with a grid one square high.

	results = []
	for x in range(1414):
		for y in bracket_target(limit, x):
			results.append(y)
	return sorted(results)[-1]


print main(100000)

