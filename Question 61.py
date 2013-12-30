    #Problem 61: Cyclical figurate numbers

import time

t1 = time.clock()

tri = []
squ = []
pent = []
hexa = []
hept = []
octa = []

for x in range(10000):              # Populate list of triangle numbers
    triangle = int(x * (x+1) / 2)

    if len(str(triangle)) == 4:
        tri.append(triangle)
    elif len(str(triangle)) > 4:
        break

for x in range(10000):              # Populate list of square numbers
    square = int(x **2)
    if len(str(square)) == 4:
        squ.append(square)
    elif len(str(square)) > 4:
        break

for x in range(10000):              # Populate list of pentagon numbers
    pentagon = int(x * (3*x -1) / 2)
    if len(str(pentagon)) == 4:
        pent.append(pentagon)
    elif len(str(pentagon)) > 4:
        break

for x in range(10000):              # Populate list of Hexagon numbers
    hexagon = int(x * (2*x -1))
    if len(str(hexagon)) == 4:
        hexa.append(hexagon)
    elif len(str(hexagon)) > 4:
        break

for x in range(10000):              # Populate list of Heptagon numbers
    heptagon = int(x * (5*x -3) / 2)
    if len(str(heptagon)) == 4:
        hept.append(heptagon)
    elif len(str(heptagon)) > 4:
        break

for x in range(10000):              # Populate list of Octagon numbers
    octagon = int(x * (3*x -2))
    if len(str(octagon)) == 4:
        octa.append(octagon)
    elif len(str(octagon)) > 4:
        break

num_table = {}                      # Format: {2556: ['tri', 'hexa'],...}

all_nums = [ x for x in tri + squ + pent + hexa +hept + octa]

for item in set(all_nums):          # Ininialize num_table with empty lists
    num_table[item] = []

for item in tri:                    # Populate num_table values.
    num_table[item].append("tri")
for item in squ:
    num_table[item].append("squ")
for item in pent:
    num_table[item].append("pent")
for item in hexa:
    num_table[item].append("hexa")
for item in hept:
    num_table[item].append("hept")
for item in octa:
    num_table[item].append("octa")

    # Now that we have our lists of each polygonal number and a dictionary
    # with each number and its polygonal types, let's start iterating through
    # them to discover ordered sets.

pairs = []                          # First we'll find the pairs
for x in octa:
    a = str(x)[-2:]
    for y in all_nums:
        if x != y:
            b = str(y)[:2] 
            if len(num_table[y]) == 1:
                if num_table[y] != num_table[x]:
                    if a == b:
                        pairs.append([x,y])
            elif a == b:
                pairs.append([x,y])

triplets = []                       # Now we'll make triplets
for double in pairs:
    x = double[0]
    y = double[1]
    a = str(y)[-2:]
    types = [num_table[x], num_table[y]]
    for z in all_nums:
        if z != x and z != y:
            b = str(z)[:2]
            if len(num_table[z]) == 1:
                if num_table[z] not in types:
                    if a == b:
                        triplets.append([x, y, z])
            elif a == b:
                triplets.append([x, y, z])

fours = []
for triplet in triplets:
    x = triplet[0]
    y = triplet[1]
    z = triplet[2]
    a = str(z)[-2:]
    types = [num_table[x], num_table[y], num_table[z]]
    for xx in all_nums:
        if xx != x and xx != y and xx != z:
            b = str(xx)[:2]
            if len(num_table[xx]) == 1:
                if num_table[xx] not in types:
                    if a == b:
                        fours.append([x, y, z, xx])
            elif a == b:
                fours.append([x, y, z, xx])

fives = []
for quadruplet in fours:
    x = quadruplet[0]
    y = quadruplet[1]
    z = quadruplet[2]
    xx = quadruplet[3]
    a = str(xx)[-2:]
    types = [num_table[x], num_table[y], num_table[z], num_table[xx]]
    for yy in all_nums:
        if yy != x and yy != y and yy != z and yy != xx:
            b = str(yy)[:2]
            if len(num_table[yy]) == 1:
                if num_table[yy] not in types:
                   if a == b:
                       fives.append([x,y,z,xx,yy])
            elif a == b:
                fives.append([x,y,z,xx,yy])
                
sixes = []
for quintuplet in fives:
    x = quintuplet[0]
    y = quintuplet[1]
    z = quintuplet[2]
    xx = quintuplet[3]
    yy = quintuplet[4]
    a = str(yy)[-2:]
    i = str(x)[:2]
    types = [num_table[x], num_table[y], num_table[z], num_table[xx], num_table[yy]]
    for zz in all_nums:
        if zz != x and zz != y and zz != z and zz != xx and zz != yy:
            b = str(zz)[:2]
            j = str(zz)[-2:]
            if len(num_table[zz]) == 1:
                if num_table[zz] not in types:
                    if a == b and i == j:
                        sixes.append([x,y,z,xx,yy,zz])
            elif a == b and i == j:
                sixes.append([x,y,z,xx,yy,zz])

answers = []                
for candidate in sixes:
    if candidate not in answers:
        answers.append(candidate)

print(sum(answers[0]))


t2 = time.clock()

print("Execution time: " + str(t2-t1)[:5])



    
"""for number, kind in num_table.items():
        if kind not in kinds:
            i = str(number)[:-2]
            j = str(number)[2:]
                if b == i:
                    ordered_set.append"""

