# Problem 5: Smallest multiple

import math

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

def main(limit):

	# Iterates through each number less than limit testing for primeness.
	# Counter is multiplied by each prime number for the a number of times
	# equal to the greatest number of times that prime divides a number less
	# than or equal to the limit.  For example, 2 divides 8 3 times (8 = 2*2*2),
	# so when limit == 10 counter is multiplied by 2^3.
	counter = 1
	for x in range(2, limit+1):
		if isPrime(x):
			counter *= (x ** math.floor(math.log(limit, x)))
	return counter

print(main(20))