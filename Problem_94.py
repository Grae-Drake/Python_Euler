# Problem 94: Almost Equilateral Triangles

import time

def get_children(tripple):
	# Takes a primitive Pythagorian tripple as input and returns a list of
	# the three "child" tripples obtained through Berggren's linear transformations.
	
	a, b, c = tripple[0], tripple[1], tripple[2]
	
	a1 = -a + (2*b) + (2*c)
	a2 = a + (2*b) + (2*c)
	a3 = a - (2*b) + (2*c)
	
	b1 = -(2*a) + b + (2*c)
	b2 = (2*a) + b + (2*c)
	b3 = (2*a) -b + (2*c)
	
	c1 = -(2*a) + (2*b) + (3*c)
	c2 = (2*a) + (2*b) + (3*c)
	c3 = (2*a) - (2*b) + (3*c)
	
	return [(a1,b1,c1), (a2,b2,c2), (a3,b3,c3)]

def list_primitive_tripples(limit):
	# Return a list of all primitive pythagorian tripples with sums below limit

	generations = [[(3, 4, 5)]]

	while True:
		next_gen = []
		for tripple in generations[-1]:
			candidates = get_children(tripple)
			for candidate in candidates:
				perimiter = sum(candidate)
				if perimiter < limit:
					next_gen.append(candidate)
		if len(next_gen) > 0:
			generations.append(next_gen)
		else:
			break

	flattened = sum(generations, [])
	return flattened

def main():
	pass
	

if __name__ == '__main__':
	t1 = time.clock()
	print len(list_primitive_tripples(10000000))
	print "Execution time: {} seconds".format(time.clock() - t1)
