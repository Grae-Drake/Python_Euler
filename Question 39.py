        # Problem 39: Interger Right Triangles

"""
    If p is the perimeter of a right angle triangle with integral length
    sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p  1000, is the number of solutions maximised?
"""

answers = []
for x in range(998):
    for y in range(998):
        z = ((x**2 + y**2)**.5)
        if z % 1 == 0:
            if x+y+z < 1000:
                answers.append(str(x+y+z))

def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(answers))
