# Problem 87: Prime Power Triples

import  C:\Users\Grae\Documents\Projects\Python_Euler\Functions\Euler

def main(limit):

	fourth_power = [x ** 4 for x in Euler.prime_sieve(int(limit **.25))]
	third_power = [x ** 4 for x in Euler.prime_sieve(int(limit ** (1/3)))]
	second_power = [x ** 4 for x in Euler.prime_sieve(int(limit ** .5))]
	print len(fourth_power)
	print len(third_power)
	print len(second_power)

main(50000000)

