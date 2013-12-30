        # Problem 29: Distinct Powers

results = []
for a in range(2,101):
    for b in range(2,101):
        results.append(a**b)

results = list(set(results))
results.sort()
print(len(results))

print(len('1'))
