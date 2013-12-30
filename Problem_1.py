# Problem 1: Multiples of 3 and 5

def main(limit):
	counter = 0
	for x in range(0,limit):
		if (x%3 == 0 or x%5 == 0):
			counter += x
	return (counter)
print(main(1000))