# Problem 29: Distinct PowersDigit Fifth Powers

import time
t0 = time.clock()

def main(power):
	results = []

	for x in range(2, 10 ** (power + 1)):
	    listx = [int(y) for y in str(x)]
	    sumofpowers = sum([y**5 for y in listx])
	    if sumofpowers == x:
	        results.append(x)
	return sum(results)

print main(5)
print "Execution time: " + str(time.clock() - t0)[:5] + " seconds."