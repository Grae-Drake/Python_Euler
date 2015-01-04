from __future__ import division

import time

t1 = time.clock()

limit = 100
digits = range(1, 10)
field = range(1, limit)

# Build empty dictionaries for decomposing a number into component numbers
# With field = 100 these take 320 milliseconds to populate.

subtraction = {digit: [] for digit in field}
addition = {digit: [] for digit in field}
division = {digit: [] for digit in field}
multiplication = {digit: [] for digit in field}

for digit in field:
    for x in field:
        for y in field:
            if y > x:

                if x - y == digit:
                    subtraction[digit].append([x, y])

                if x + y == digit:
                    addition[digit].append([x, y])

                if y / x == digit:
                    division[digit].append([x, y])

                if x * y == digit:
                    multiplication[digit].append([x, y])

print time.clock() - t1


# Ok, we've built the decomposition dicts, time to start using them!
# More to come here.
for x in field:
    if len(division[x][0]) == 1:
        print x
