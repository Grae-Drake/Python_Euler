# Problem 25
# 1,000 digit Fibonacci number

fibs = [1,1]

while len(str((fibs[-1])))<1000:
    newnum = fibs[-1] + fibs [-2]
    fibs.append(newnum)

print(len(fibs))
print(fibs[-1])
