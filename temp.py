
# Problem 26
 # Reciprocal cycles
 
results = []
for n in range(1,3):
    finished = False
    repeater = []
    count = 0
    while finished == False:
        digit = ((10**count)//n)* n
        if ((10**count)/float(n)) == 0:
            finished  = True
        elif digit in repeater:
            finished = True
            repeater.append(digit)
        else:
            repeater.append(digit)
            count += 1
    results.append([n, repeater])
 
print(results)