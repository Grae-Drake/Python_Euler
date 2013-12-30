        # Problem 56: Powerful Digit Sum
        # Considering natural numbers of the form, a^b, where a, b < 100,
        # what is the maximum digital sum?
import time
t1 = time.clock()

def digit_sum(number):
    # returns the sum of each digit in number
    counter = 0
    for x in str(number):
        counter += int(x)
    return counter

answer = 0
n1 = 0
n2 = 0
for x in range(1, 100):
    for y in range(1, 100):
        testnum = digit_sum(x**y)
        if testnum > answer:
            answer = testnum
            n1 = x
            n2 = y
t2 = time.clock()
print("the digit sum of " + str(n1) + "^" + str(n2) + "equals: " + str(answer))

print("Executing time: " + str(t2-t1)[:7] + " seconds.")

