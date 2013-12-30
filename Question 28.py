        # Problem 28: Number Spiral Diagonals

side = 1001
n = side**2
diagonals = [n]

for x in range(int((side-1)/2)):
    for y in range(4):
        n = n - ((side-1)-2*x)
        diagonals.append(n)

print(sum(diagonals))
    
