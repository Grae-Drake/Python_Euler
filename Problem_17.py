# Problem 17: Number letter counts

# Populate the initial members of a dictionary.  We'll build the remaining
# entries from these initial ones.
numbers = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
    8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60:
    "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 1000: "OneThousand"}

def populateNumbers():

    # This function searches the dictionary for each number below 1000 and
    # adds a new entry if it's not already in there.
    for item in range(1,1000):
        if item not in numbers:
            newValue = ""
            digitsReversed = [int(x) for x in str(item)[::-1]]
            for index, digit in enumerate(digitsReversed):
                if digit:       # Ignore digits when they're 0
                    if index == 0:
                        if digitsReversed[1] == 1:
                            pass
                        else:
                            newValue = numbers[digit] + newValue
                    if index == 1:
                        if digit == 1:
                            newValue = numbers[digitsReversed[0] + 10] + newValue
                        else:
                            newValue = numbers[digit * 10] + newValue
                    if index == 2:
                        if digitsReversed[0] + digitsReversed[1] != 0:
                            newValue = numbers[digit] + "Hundred" + "And" + newValue
                        else:
                            newValue = numbers[digit] + "Hundred" + newValue
            numbers[item] = newValue

def main():
    populateNumbers()
    result = 0
    for value in numbers.values():
        result += len(value)
    return result

print main()