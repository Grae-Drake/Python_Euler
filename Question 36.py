        # Problem 36: Double-base Palindromes


""" The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in
    base 10 and base 2. (Please note that the palindromic number, in either base,
    may not include leading zeros.)
"""

answers = []
for x in range(1000000):
    strx = str(x)
    paltest = True
    for y in range(len(strx)//2):
        if strx[y] != strx[len(strx)-(y+1)]:
            paltest = False
    if paltest == True:
        strbinx = bin(x)[2:]
        binpaltest = True
        for z in range(len(strbinx)//2):
            if strbinx[z] != strbinx[len(strbinx)-(z+1)]:
                binpaltest = False
        if binpaltest == True:
            answers.append(x)

print(sum(answers))
