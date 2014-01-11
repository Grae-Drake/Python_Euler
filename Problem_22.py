# Problem 22: Names Scores

# First, let's make a sorted list of the names:
file_path = "/Users/graedrake/Documents/Projects/Python_Euler/TextFiles/problem_22_names.txt"
names_file = open(file_path)
names_str = names_file.read()                   # Read the file into a string
names_file.close()                              # Close the file
names_str1 = names_str[1:-1]                    # Delete the first and last ""s
names_list = sorted((names_str1.split('","')))  # Split and sort

# Dictionary with letter scores
alphabet = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
    "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
    "W": 23, "X": 24, "Y": 25, "Z": 26
    }

def score_name(name):

    # Returns the name score of the input name
    return sum([alphabet[letter] for letter in name])

def main():

    # returns the sum of each name score times each name index in names_list
    return sum([index * score_name(name) for index, name in enumerate(names_list, start=1)])

print(main())




