# Problem 94: Almost Equilateral Triangles

import time
import math

def get_tripples(m,n):


	"""Return pythagorean tripples a, b and c given m and n."""

	a = (m ** 2) - (n ** 2)
	b = 2 * m * n
	c = (m ** 2) + (n ** 2)
	return a, b, c

def get_even_bases(limit):


	"""
	Look for pythagorean tripples describing one half of an 'almost'
	equilateral triangle with perimeters below limit and an even base length.
	Return the sum of the perimeters of each such triangle.
	"""

	answer = 0
	perimeter = 0
	almost_equilateral_triangles = []
	root_three = 3 ** .5
	m  = 2

	while perimeter < limit:
		n = math.floor(m / root_three)
		tripples = get_tripples(m, n)
		perimeter = (tripples[0] + tripples[2]) * 2
		if abs(tripples[2] - (tripples[0] * 2)) == 1 and perimeter < limit:
			almost_equilateral_triangles.append(tripples)
			answer += perimeter
			print "Tripple: {}; Perimeter: {}; m: {}; n: {}".format(tripples, perimeter, m, n)
		m += 1

	return answer

def get_odd_bases(limit):


	"""
	Look for pythagorean tripples describing one half of an 'almost'
	equilateral triangle with perimeters below limit and an odd base length.
	Return the sum of the perimeters of each such triangle.
	"""

	answer = 0
	perimeter = 0
	almost_equilateral_triangles = []
	root_three = 3 ** .5
	m = 2

	while perimeter < limit:
		n = math.ceil(m / root_three)
		tripples = get_tripples(m, n)
		perimeter = tripples[0] + tripples[2]
		if abs((tripples[0] * 2) - tripples[2]) == 2 and perimeter < limit:
			almost_equilateral_triangles.append(tripples)
			answer += perimeter
		m += 1

	return answer

def main(limit):
	return get_even_bases(limit) + get_odd_bases(limit)

if __name__ == '__main__':
	t1 = time.clock()
	print main(1000000000)
	print "Execution time: {} seconds".format(time.clock() - t1)
