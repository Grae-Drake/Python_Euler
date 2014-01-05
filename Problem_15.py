# Problem 15: Lattice paths

import math

def main(length):
	return (math.factorial(length * 2) / (math.factorial(length) ** 2))

print main(20)
