        # Problem 42: Coded Triangle Numbers

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # Create a dictionary
mydict = dict([(item, index+1) for index, item in enumerate(letters)])

trinums = []                                # Create a list of triangular numbers.
counta = 1                                  # The less lazy way would be 
countb = 2                                  # to create a checking function...
while counta < 1000:
    trinums.append(counta)
    counta+=countb
    countb+=1
                                            # Put all the words in a list
f = open("Problem 42 Words.txt")
wordstring = f.read()
f.close()
for char in '",':
    wordstring = wordstring.replace(char," ")
wordlist = wordstring.split()

def wordValue(word):                        # Create a function to calculate
    counter = 0                             # word values
    for letter in word:
        counter += mydict[letter]
    return counter

answers = []                                # Run the function against the list
for word in wordlist:
    if wordValue(word) in trinums:
        answers.append(word)

print(len(answers))


