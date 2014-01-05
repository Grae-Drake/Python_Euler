# Problem 17: Number letter counts

# Populate the initial members of a dictionary.  We'll build the remaining
# entries from these initial ones.
numbers = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
    8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60:
    "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 1000: "OneThousand"}

def getNumberString(number, numbers):

    # Takes an integer and returns a string describing that integer.
    # Ex: getNumberString(145) returns "OneHundredFourtyFive".
    newValue = ""
    digitsReversed = [int(x) for x in str(number)[::-1]]
    for index, digit in enumerate(digitsReversed):
        if digit:                               # Ignore digits when they're 0
            if index == 0:                      # Start with the ones digit
                if digitsReversed[1] == 1:
                    pass                        # Deal with 11-19 with the tens digit
                else:
                    newValue = numbers[digit] + newValue
            if index == 1:                      # Process the tens digit
                if digit == 1:                  # Now we address 11-19
                    newValue = numbers[digitsReversed[0] + 10] + newValue
                else:
                    newValue = numbers[digit * 10] + newValue
            if index == 2:                      # Process the hundreds digit
                if digitsReversed[0] + digitsReversed[1] != 0:
                    newValue = numbers[digit] + "Hundred" + "And" + newValue
                else:
                    newValue = numbers[digit] + "Hundred" + newValue
    return newValue

def populateNumbers(numbers):

    # Start with minimally populated dictionary, iterating through range(1,1000)
    # and adding new entries if not already there.  Returns the dictionary.
    for number in range(1,1000):
        if number not in numbers:
            numbers[number] = getNumberString(number, numbers)
    return numbers

def main():

    # Invoke populateNumbers() and sum all strings in the full dictionary
    result = 0
    for value in populateNumbers(numbers).values():
        result += len(value)
    return result

print main()