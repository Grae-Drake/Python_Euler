        # Problem 55: Lychrel numbers
        # How many Lychrel numbers are there below 10,000?

import math

def is_palindrome(number):
    # Returns True if number is a palindrome.  Else returns False.

    number = str(number)
    result = True
    for index, item in enumerate(number):
        if index < math.ceil(len(number)/2):
            if number[index] != number[-1 - index]:
                result = False
    return result

answers = []
for x in range(1, 10001):
    seed = x
    counter = 0
    candidate = seed
    while counter <= 50:
        candidate += int(str(candidate)[::-1])
        counter += 1
        if is_palindrome(candidate) == True:
            break
        if counter > 50:
            answers.append(seed)

print(len(answers))

