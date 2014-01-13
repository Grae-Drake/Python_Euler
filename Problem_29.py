# Problem 29: Distinct Powers

def main(a,b):

	# Returns the number of unique values produced by x**y for 1 < x < a
	# and 1 < y < b.
	results = []
	for x in range(2,a):
	    for y in range(2,b):
	        results.append(x**y)
	return len(list(set(results)))

print main(101,101)
