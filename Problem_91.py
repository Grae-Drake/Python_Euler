# Problem 92: Right triangles with integer coordinates

import time, itertools

class Triangle(object):
	""" Triangle with three points, one of which is at the origin """

	def __init__(self, p1x, p1y, p2x, p2y):

		self.p1x = p1x
		self.p1y = p1y
		self.p2x = p2x
		self.p2y = p2y

		self.side1_square = self.p1x ** 2 + self.p1y ** 2
		self.side2_square = self.p2x ** 2 + self.p2y ** 2
		self.side3_square = (self.p1x - self.p2x) ** 2 + (self.p1y - self.p2y) ** 2

		self.a_square = sorted([self.side1_square, self.side2_square, self.side3_square])[0]
		self.b_square = sorted([self.side1_square, self.side2_square, self.side3_square])[1]
		self.c_square = sorted([self.side1_square, self.side2_square, self.side3_square])[2]

		self.is_right = self.a_square + self.b_square == self.c_square

def main(grid_size):

	"""
	Return the number of right trianges existing with two points at integer
	coordinates and the third at the origin with 0 <= x1, y1, x2, y2 <= grid_size.
	"""

	# Generate the coordinate plane and coordinate pairs.
	# Remember to strip out the origin from the coordinate plane.
	coordinate_plane = itertools.product(range(grid_size + 1), repeat=2)
	coordinate_plane = (x for x in coordinate_plane if x != (0,0))
	coordinate_pairs = itertools.permutations(coordinate_plane, 2)

	# Iterate through the triangles defined by the coordinate_pairs.
	count = 0
	for points in coordinate_pairs:	
		triangle = Triangle(points[0][0], points[0][1], points[1][0], points[1][1])
		if triangle.is_right:
			count += 1
	return count

if __name__ == '__main__':
	t1 = time.clock()
	print main(50)
	print "Execution time = {} seconds".format(time.clock() - t1)