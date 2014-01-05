# Problem 13: Large sum

def main():

	# Returns the first 10 digits of the sum of each of the numbers
	# in "Problem_13_Grid.txt"

	data = open("/Users/graedrake/Documents/Projects/Python_Euler/TextFiles/Problem13Data.txt")
	return str(sum([int(str(line).rstrip()) for line in data]))[:10]

print main()

