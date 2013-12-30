        # Problem 38: Interger Right Triangles

"""
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192  1 = 192
    192  2 = 384
    192  3 = 576
    
    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3).

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n  1?
"""

# Possibilities: 1-2-2-2-2 (only 9), 2-2-2-3, 3-3-3, 4-5

f = open("1-9 pandigitals.txt")

bigstring = f.read()

f.close()

biglist = bigstring.split()
#biglist = biglist[:100]
twotwotwothree = []
threethreethree = []
fourfive = []

for item in biglist:                    #Let's check the 2-2-2-3s
    a = int(item[0:2])
    b = int(item[2:4])
    c = int(item[4:6])
    d = int(item[6:])
    panCheck = True
    if d != 4*a:
        panCheck = False 
    if c != 3*a:
        panCheck = False
    if b != 2*a:
        panCheck = False
    if panCheck == True:
        twotwotwothree.append(item)

for item in biglist:                    #Let's check the 3-3-3s
    a = int(item[0:3])
    b = int(item[3:6])
    c = int(item[6:])
    panCheck = True
    
    if c != 3*a:
        panCheck = False 
    if b != 2*a:
        panCheck = False
    if panCheck == True:
        threethreethree.append(item)

for item in biglist:                    #Let's check the 4-5s
    a = int(item[0:4])
    b = int(item[4:])
    panCheck = True
    
    if b != 2*a:
        panCheck = False 
    if panCheck == True:
        fourfive.append(item)

answers = twotwotwothree + threethreethree + fourfive
answers.sort()

#print("2-2-2-3: " + str(twotwotwothree))
#print("3-3-3: " + str(threethreethree))
#print("4-5: " + str(fourfive))

print(answers[-1])



