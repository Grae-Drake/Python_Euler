    # Problem 22: Names Scores

    # First, let's make a sorted list of the names:

names_file = open("problem_22_names.txt")   # Open the file
names_str = names_file.read()               # Read the file into a string
names_file.close()                          # Close the file
names_str1 = names_str[1:-1]                # Delete the first and last ""s
names_list = (names_str1.split('","'))      # Split the string and make a list
names_list.sort()                           # Sort the list alphabetically

    # Now we have a sorted list of strings.
    # Let's make that into a sorted list of lists, where
    # each sub-list has the name-string, the index in
    # the list (starting at 1) and the number value of the name.

big_list = []
for index, item in enumerate(names_list, start=1):
    big_list.append([item, index, [0]])

    # Now we need to calculate and assign the number values for each name.
    # Let's start by creating a dictionary with letter values

alphabet = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
    "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
    "W": 23, "X": 24, "Y": 25, "Z": 26
    }

    # Let's loop over the first element of each element in the big_list,
    # iterate over the string to create a list of numbers (by reference
    # to the dictionary 'alphabet', replace the [0] in each entry
    # with the list of numbers we generated, and finally replace that list
    # of numbers with a som of those numbers

for entry in big_list:
    for letter in entry[0]:
        entry[2].append(alphabet[letter])
    entry[2] = sum(entry[2])

    # All that's left to do is sum multiply the second and third elements
    # and sum the products

answer = 0

for entry in big_list:
    answer += (entry[1]*entry[2])

print(answer)




