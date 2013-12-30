        # Problem 34: Digit factorials

# Note: the number must be 7 digits or less, as 8*(9!) is only 7 digits.
# The largest number we need to check is 9,999,999 --> 2,540,160
#  999,999 --> 2,177,280

import math

answers = []

for x in range(3, 254160):
    counter = 0
    for y in str(x):
        counter += math.factorial(int(y))
    if counter == x:
        answers.append(x)

print(sum(answers))


