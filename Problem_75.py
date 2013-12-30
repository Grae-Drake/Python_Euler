    # Problem 75: Singular integer right triangles.
    # First try (149565) is incorrect

import time
t1 = time.clock()

def children(tripple):
    # Takes a primitive Pythagorian tripple as input and returns a list of
    # the three "child" tripples obtained through Berggren's linear transformations.

    a = tripple[0]
    b = tripple[1]
    c = tripple[2]

    a1 = -a + (2*b) + (2*c)
    a2 = a + (2*b) + (2*c)
    a3 = a - (2*b) + (2*c)

    b1 = -(2*a) + b + (2*c)
    b2 = (2*a) + b + (2*c)
    b3 = (2*a) -b + (2*c)

    c1 = -(2*a) + (2*b) + (3*c)
    c2 = (2*a) + (2*b) + (3*c)
    c3 = (2*a) - (2*b) + (3*c)

    return [(a1,b1,c1), (a2,b2,c2), (a3,b3,c3)]
    
    # Now let's generate all of the tripples with sums (lengths) below the limit
    # and add those lengths to a list.

limit = 1500001
tripples = [[(3, 4, 5)]]
lengths = [12]
    
while True:
    next_gen = []
    for tripple in tripples[-1]:
        candidates = children(tripple)
        for candidate in candidates:
            length = sum(candidate)
            if length < limit:
                next_gen.append(candidate)
                lengths.append(length)
    if len(next_gen) > 0:
        tripples.append(next_gen)
    else:
        break

    # Finally, let's create an array of numbers from 1 to limit and keep track of
    # how many lengths each number is a multiple of.
    # For the answer we just count up each number that is a multiple of only one
    # length.

array = [[x,0] for x in range(1, limit)]

for length in lengths:
    for multiple in range(length, limit, length):
        array[multiple-1][1] += 1

count = 0
for x in array:
    if x[1] == 1:
        count += 1

print count
 
t2 = time.clock()

print "Execution time: ", str(t2-t1)
