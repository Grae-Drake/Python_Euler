        # Problem 29: Distinct PowersDigit Fifth Powers

results = []

for x in range(2, 1000000):
    listx = [int(y) for y in str(x)]
    powers = [y**5 for y in listx]
    sumofpowers = sum(powers)
    if sumofpowers == x:
        results.append([x, sumofpowers])

print(results)
