    # Problem 18: Maximum path sum

triangle = []
t = open("triangle.txt")
for line in t:
    triangle.append(line.split())
t.close()

triangle2 = []
for x in triangle:
    newx = []
    for y in x:
        newx.append(int(y))
    triangle2.append(newx)
print(triangle2)

triangle3 = [triangle2[-1]]
count = 2
while count < 101:
    line2 = []
    for index, y in enumerate(triangle2[-count]):
        a = triangle3[-1][index]
        b = triangle3[-1][index+1]
        line2.append(y + max(a, b))
    triangle3.append(line2)
    count += 1

print(triangle3[-1])

