    # Problem 68: Magic 5-gon ring

import time
t1 = time.clock()


answer = [0,0,0,0,0,0,0,0,0,0]
digit = 1
position = 0
sums = 0
result = 0

while True:
    if digit > 10:
        if position == 0:
            print("Position 0 can't be greater than 10!")
            break
        else:
            digit = answer[position -1] + 1
            answer[position -1] = 0
            position -= 1
    elif digit not in answer:
        if position <= 4:
            answer[position] = digit
            digit = 1
            position += 1
        else:
            test = 0
            if position == 5:
                sums = (answer[0] + answer[1] + digit)
                test = sums
            elif position == 6:
                test = (answer[1] + answer[2] + digit)
            elif position == 7:
                test = (answer[2] + answer[3] + digit)
            elif position == 8:
                test = (answer[3] + answer[4] + digit)
            elif position == 9:
                test = (answer[4] + answer[0] + digit)
            if test == sums:
                answer[position] = digit
                if position < 9:
                    digit = 1
                    position += 1
                else:
                    if 10 not in answer[:5]:
                        print("Sum: ", sums)
                        a = (str(answer[5]) + str(answer[0]) + str(answer[1]))
                        b = (str(answer[6]) + str(answer[1]) + str(answer[2]))
                        c = (str(answer[7]) + str(answer[2]) + str(answer[3]))
                        d = (str(answer[8]) + str(answer[3]) + str(answer[4]))
                        e = (str(answer[9]) + str(answer[4]) + str(answer[0]))
                        if answer[5] == 6:
                            print(a,b,c,d,e)
                            if int(a+b+c+d+e) > result:
                                result = int(a+b+c+d+e)
                    
                    if answer[4] != 10:
                        digit = 1
                        position = 5
                        answer[5] = answer[6] = answer[7] = answer[8] = answer[9]= 0
                        answer[4] += 1
                    else:
                        digit = 1
                        position = 4
                        answer[4] = answer[5] = answer[6] = answer[7] = answer[8] = answer[9]= 0
                        answer[1] += 1
            else:
                digit += 1
    else:
        digit += 1

print("The answer is: ", result)
        


        

t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
