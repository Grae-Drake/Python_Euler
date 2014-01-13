# Problem 28: Number Spiral Diagonals

def main(side):

	# Returns the sum of the numbers on the diagonal of a spiral square
	# of side length side
	if side % 2 == 0:
		raise Exception("Side length must be odd!")
	n = side**2
	diagonals = [n]
	for x in range(int((side-1)/2)):
	    for y in range(4):
	        n = n - ((side-1)-2*x)
	        diagonals.append(n)

	return(sum(diagonals))

print main(1001)
	    
