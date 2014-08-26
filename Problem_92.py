# Problem 92: Square digit chains

# Sets to contain numbers converging to 1 and to 89.
# Using sets because hashable
ones = set(1)
eighty_nines = set(89)

def next_square_digit(n):

	""" Given n, returns the sum of the squares of the digits of n"""

	digits = [int(x) for x in str(n)]
	total = 0
	for digit in digits:
		total += digit ** 2
	return total

def main():
	print next_square_digit(58)

if __name__ == '__main__':
	main()