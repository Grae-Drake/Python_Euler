# Problem 1: Multiples of 3 and 5

def generate_fibonaccis(limit):

	# Returns a list of all Fibonacci numbers less than limit
	fibonaccis = [1,1]
	term1 = 1
	term2 = 1
	while term1 + term2 < limit:
		candidate = term1 + term2
		fibonaccis.append(candidate)
		term1, term2 = candidate, term1
	return fibonaccis

def evenSum(numList):
	
	# Returns the sum of all even numbers in the list provided
	evenSum = 0
	for x in numList:
		if x % 2 == 0:
			evenSum += x
	return evenSum

def main(limit):	

	return(evenSum(generate_fibonaccis(limit)))
	
print(main(4000000))