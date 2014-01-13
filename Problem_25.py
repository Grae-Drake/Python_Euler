# Problem 25: 1,000 digit Fibonacci number

import time
t0 = time.clock()

def first_n_digit_fibonacci_number(n):

	# Returns the index number of the first Fibonacci number with n digits.
	fibs = [1,1]
	while len(str((fibs[-1]))) < n:
	    newnum = fibs[-1] + fibs [-2]
	    fibs.append(newnum)
	return len(fibs)

print first_n_digit_fibonacci_number(1000)
print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."