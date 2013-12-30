        # Problem 43: Sub-String Divisibility

def panCheck(*numbers):
    # Accepts an arbitrary number of strings and
    # returns True if no character appears more than once.
    startList = []
    for item in numbers:
        for i in item:
            startList.append(i)
    startList.sort()
    endList = []
    lookup = []
    for item in startList:
        if item not in lookup:
            endList.append(item)
            lookup.append(item)
    if startList == endList:
        return True
    if startList != endList:
        return False

seeds = []                      # Build a list of seeds.  Let's work backwards.
for x in range(1,59):
    testnum = str(x*17)
    if panCheck(testnum) == True:
        if len(testnum) > 2:
            seeds.append(testnum)
        else:
            seeds.append("0"+testnum)

step2 = []
for seed in seeds:              # Build the second element
    for x in range(10):
        if panCheck(str(x), seed) == True:
            testnum = str(x)+seed
            if int(testnum[:3]) % 13 == 0:
                step2.append(testnum)

step3 = []
for item in step2:
    for x in range(10):
        if panCheck(str(x), item) == True:
            testnum = str(x)+item
            if int(testnum[:3]) % 11 == 0:
                step3.append(testnum)

step4 = []
for item in step3:
    for x in range(10):
        if panCheck(str(x), item) == True:
            testnum = str(x)+item
            if int(testnum[:3]) % 7 == 0:
                step4.append(testnum)

step5 = []
for item in step4:
    for x in range(10):
        if panCheck(str(x), item) == True:
            testnum = str(x)+item
            if int(testnum[:3]) % 5 == 0:
                step5.append(testnum)

step6 = []
for item in step5:
    for x in range(10):
        if panCheck(str(x), item) == True:
            testnum = str(x)+item
            if int(testnum[:3]) % 3 == 0:
                step6.append(testnum)

step7 = []
for item in step6:
    for x in range(10):
        if panCheck(str(x), item) == True:
            testnum = str(x)+item
            if int(testnum[:3]) % 2 == 0:
                step7.append(testnum)

answers = []
for item in step7:
    for x in range(10):
        testnum = str(x)+item
        if panCheck(testnum) == True:
            #if len(testnum) == 10:
                answers.append(int(testnum))
        
answer = 0
for item in answers:
    answer += int(item)

print(answer)












