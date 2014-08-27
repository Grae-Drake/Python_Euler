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

grid_size = 2

point_field = itertools.product(range(grid_size + 1), repeat=2)
point_pairs = itertools.permutations(point_field, 2)