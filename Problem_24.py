# Problem 24: Lexicographic permutations

import itertools

def nth_lexigraphic_permutation(n, objects):

	# Returns a tuple containing the nth lexigraphic permutation of objects
	return [x for x in itertools.permutations(objects)][n-1]

print nth_lexigraphic_permutation(1000000, [0,1,2,3,4,5,6,7,8,9])
