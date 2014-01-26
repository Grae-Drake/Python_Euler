# Problem 88: Product-sum numbers

import  Euler, time

t0 = time.clock()

def main(limit):
	result = 0
	k = 0
	n = 4
	primes = [2]

	def prime_factors(n):

	    # Return a list of the prime factors of n.
	    while n > primes[-1]:
	    	primes.append(Euler.next_prime(primes[-1]))
	    candidates = primes
	    result = []
	    for prime in candidates:
	        while True:
	            if n % prime == 0:
	                result.append(prime)
	                n = n / prime
	            else:
	                break
	    return result

	while k < limit:
		n_factors = prime_factors(n)
		if len(n_factors) == 0:
			pass
		else:
			set_length = len(n_factors) + n - sum(n_factors)
			if set_length > k:
				k = set_length
				result += n
				print "For k = {}, n = {}.".format(k,n)
		n += 1
	return result

print main(12)

print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."


