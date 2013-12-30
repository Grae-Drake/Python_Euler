factors = []
big = []
check = 1

number = 600851475143
root = 775147
for x in range(2, root):
        if number % x == 0:
                factors.append(x)
for x in factors:
        y = number/x
        big.append(y)

for x in factors:
        check = check*x
        
print(factors)
print(big)
print(check)
