M = 80
count = 0
for x in range(1,M):
	for y in range(1,M):
		for z in range(1,M):
			ordered = sorted([x,y,z])
			a = ordered[0]
			b = ordered[1]
			c = ordered[2]

			hyp = ((a+b)**2 + c**2)**.5
			if int(hyp) == hyp:
				count += 1

print count
