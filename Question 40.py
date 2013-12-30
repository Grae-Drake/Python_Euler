        # Problem 40: Champernowne's constant

"""
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, find the value of the following expression:
    d1  d10  d100  d1000  d10000  d100000  d1000000
"""

import time
t1 = time.clock()

bigstring = ""

for x in range(1,200000):
    bigstring += str(x)

t2 = time.clock()
print(t2-t1)

d1 = int(bigstring[0])
d2 = int(bigstring[9])
d3 = int(bigstring[99])
d4 = int(bigstring[999])
d5 = int(bigstring[9999])
d6 = int(bigstring[99999])
d7 = int(bigstring[999999])

t3 = time.clock()
print(t3-t2)
print(d1*d2*d3*d4*d5*d6*d7)

print(bigstring[:12])




