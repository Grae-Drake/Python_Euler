# Problem 85: Counting rectangles

import math

def count_rectangles(height,width):

	# Returns the number of component rectangles in a rectangular height by width grid.
	return height * (height+1) * width * (width+1) / 4

def bracket_target(limit, height):

	# Returns a tuple containing the largest count_rectangles(height, width) less
	# than limit and the smallest count_rectangles(height, width) greater than limit.

	testnum = 0
	width = 0
	while testnum < limit:
		width += 1
		testnum = count_rectangles(height, width)
		
	return ([count_rectangles(height, width), height * width], [count_rectangles(height, width-1), height * (width-1)])

def main(limit):
	rectangles = 0
	area = None

	# Here we calculate the root of the quadratic equation in count_rectangles()
	# with height set to 1 and round up.
	side = int(math.ceil(((8 * limit + 1) ** .5 -1) / 2))

	for x in range(1, side + 1):
		for y in bracket_target(limit, x):
			if abs(limit - y[0]) < abs(limit - rectangles):
				rectangles = y[0]
				area = y[1]

	return area

print main(2000000)