# Problem 6: Sum square difference

def squareOfSum(n):

	# Returns the square of the sum of all natural numbers through n.
	return sum(list(range(n+1))) ** 2

def sumOfSquares(n):

	# Returns the sum of all squares of all natural numbers through n.
	result = 0
	for x in range(n + 1):
		result += x ** 2
	return result

def main(limit):
	return (squareOfSum(limit) - sumOfSquares(limit))

print(main(100))