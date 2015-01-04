from __future__ import division

import time

t1 = time.clock()

limit = 100
digits = range(1, 10)
field = range(1, limit)

# Build empty dictionaries for decomposing a number into component numbers
# With field = 100 these take 17 milliseconds to populate.

subtraction = {}
addition = {}
division = {}
multiplication = {}

for x in field:
    for y in field:
        if y > x:

            sub = y - x
            if sub not in subtraction:
                subtraction[sub] = []
            subtraction[sub].append(sorted([x, y]))

            add = y + x
            if add not in addition:
                addition[add] = []
            addition[add].append(sorted([x, y]))

            mult = y * x
            if mult not in multiplication:
                multiplication[mult] = []
            multiplication[mult].append(sorted([x, y]))

            if y % x == 0:
                div = y / x
                if div not in division:
                    division[div] = []
                division[div].append(sorted([x, y]))

print division[20]
print time.clock() - t1


# Ok, we've built the decomposition dicts, time to start using them!
# More to come here.

# for x in field:
#     if len(division[x][0]) == 1:
#         print x
