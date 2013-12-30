# Problem 3: Largest Prime Factor

def isPrime(n):

	# Returns True if n in prime; otherwise returns False
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n ** 0.5)
	f = 5
	while f <= r:
		if n % f == 0: return False
		if n % (f + 2) == 0: return False
		f += 6
	return True

def generatePrimeFactors(n):

	# Returns a sorted list of the prime factors of n.
	factors = []
	for x in range(2, int(n ** .5)):
		if n % x == 0:
			cofactor = n / x
			if isPrime(x):
				factors.append(x)
			if isPrime(cofactor):
				factors.append(cofactor)
	factors.sort()
	return factors

# Print the final element in the list of prime factors
print(generatePrimeFactors(600851475143)[-1])
