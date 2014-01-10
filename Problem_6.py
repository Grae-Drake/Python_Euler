# Problem 6: Sum square difference

def square_of_sum(n):

	# Returns the square of the sum of all natural numbers through n.
	return sum(list(range(n+1))) ** 2

def sum_of_squares(n):

	# Returns the sum of all squares of all natural numbers through n.
	result = 0
	for x in range(n + 1):
		result += x ** 2
	return result

def main(limit):
	return (square_of_sum(limit) - sum_of_squares(limit))

print(main(100))