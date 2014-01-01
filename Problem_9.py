# Problem 9: Special Pythagorean triplet

import math

def main(n):
	for a in range(1, n):
		for b in range(1, n):
			c = math.sqrt((a ** 2) + (b ** 2))
			if c % 1 == 0 and (a + b + c) == n:
				print [a,b,c]
				return (a * b * c)
	return "There is no Pythagorean triplet for which a + b + c = " + str(n) + "."

print(main(1000))