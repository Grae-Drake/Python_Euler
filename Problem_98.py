"""
    By replacing each of the letters in the word CARE with 1, 2, 9, and 6
    respectively, we form a square number: 1296 = 362. What is remarkable is
    that, by using the same digital substitutions, the anagram, RACE, also
    forms a square number: 9216 = (96 ** 2). We shall call CARE (and RACE) a
    square anagram word pair and specify further that leading zeroes are not
    permitted, neither may a different letter have the same digital value as
    another letter.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, find all the square
    anagram word pairs (a palindromic word is NOT considered to be an anagram
    of itself).

    What is the largest square number formed by any member of such a pair?

    NOTE: All anagrams formed must be contained in the given text file.
"""

import time


def main():

    # Read the given wordfile and populate a list.
    with open("TextFiles/p098_words.txt") as word_file:
        words_list = word_file.readlines()[0].rsplit(',')

    # Strip out words with more than 10 unique letters.
    words_list = [x.strip('"') for x in words_list if
                  len(set(x.strip('"'))) <= 10]

    # Group words of similar length together in a dictionary.
    word_dict = {}
    for word in words_list:
        if len(word) not in word_dict:
            word_dict[len(word)] = [word]
        else:
            word_dict[len(word)].append(word)

    # Filter out words with no anagrams and group anagrams together.
    for n in range(1, max(word_dict.keys()) + 1):
        anagrams = []
        for word in word_dict[n]:

            word_signature = "".join(sorted(word))

            for compare in word_dict[n]:
                if compare != word:
                    compare_signature = "".join(sorted(compare))
                    if compare_signature == word_signature:
                        anagrams.append(tuple(sorted([word, compare])))
        word_dict[n] = list(set(anagrams))
        print "{} digit anagrams: {}\n".format(n, word_dict[n])


if __name__ == "__main__":

    t1 = time.clock()

    print main()

    print time.clock() - t1
