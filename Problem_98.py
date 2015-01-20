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
import itertools

# Build dictionary of square numbers (with a reference to their root).
square_nums = {}
for x in xrange(1, 31427):
    square_nums[x ** 2] = x

print 1369 in square_nums


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

    # Gather all anagram pairs.
    anagram_pairs = []
    for n, words in word_dict.iteritems():

        for word in words:
            word_signature = "".join(sorted(word))

            for compare in words:
                compare_signature = "".join(sorted(compare))

                if compare == word:
                    continue
                if compare_signature == word_signature:
                    anagram_pairs.append(tuple(sorted([word, compare])))

    anagram_pairs = sorted(list(set(anagram_pairs)),
                           key=lambda x: len(x[0]),
                           reverse=True)

    for pair in anagram_pairs:
        print "Testing {}".format(pair)
        print process_anagram(pair)


def process_anagram(pair):

    # Take an anagram pair as input. Apply each permutation of digits to the
    # first word and evaluate result in second word.

    matching_pairs = []
    word = pair[0]
    compare = pair[1]
    permutations = itertools.permutations(range(10), len(pair[0]))

    for permutation in permutations:
        if permutation[0] == 0:
            continue

        letter_map = dict(zip(word, permutation))

        n1 = int("".join([str(n) for n in permutation]))
        if n1 not in square_nums:
            continue

        n2 = int("".join([str(letter_map[letter]) for letter in compare]))
        if n2 not in square_nums:
            continue
        matching_pairs.append({n1: word, n2: compare})
    return matching_pairs


if __name__ == "__main__":

    t1 = time.clock()

    print main()

    print time.clock() - t1
