        # Problem 57: Square root convergents

import time
t1 = time.clock()

counter = 0
answer = [[1, 3, 2], [2, 7, 5], [3, 17, 12], [4, 41, 29], [5, 99, 70]]

while len(answer) < 999:
    expansion = answer[-1][0] + 1
    numerator = (answer[-1][1] * 2) + answer[-2][1]
    denominator = (answer[-1][2] * 2) + answer[-2][2]
    answer.append([expansion, numerator, denominator])

for x in answer:
    if len(str(x[1])) > len(str(x[2])):
        counter += 1

t2 = time.clock()

print("The answer is " + str(counter))
print("Execution time = " + str(t2-t1)[:5] + " seconds")
