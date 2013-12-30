pallindrome = []
range999 = []
for i in range(1,1000):
        range999.append(i)
for i in range999:
        for x in range(1,1000):
                temp = x*i
                check1 = str(temp)
                check2 = check1[::-1]
                if check1 == check2:
                        pallindrome.append(temp)
                
pallindrome.sort()
print(pallindrome)

