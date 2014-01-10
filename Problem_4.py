# Problem 4: Largest Palindrome Product
def is_pallindrome(n):

	# Returns True if n is a palindrome, otherwise returns False.
	if str(n) == str(n)[::-1]:
		return True
	else:
		return False

def main(limit):

	# Returns the largest palindrome that is the product of two
	# limit-digit numbers.
	pallindrome = []
	for i in range(10 ** (limit-1), 10 ** limit):
		for j in range(10 ** (limit-1), 10 ** limit):
			candidate = i * j
			if is_pallindrome(candidate):
				pallindrome.append(candidate)
	pallindrome.sort()
	return pallindrome[-1]

print(main(3))

