    # Problem 68: Magic 5-gon ring

import time
t1 = time.clock()


answer = [0,0,0,0,0,0,0,0,0,0]
digit = 1
position = 1
sums = 0
afound = False
bfound = False
cfound = False
dfound = False
efound = False
ffound = False
gfound = False
hfound = False
ifound = False
jfound = False

while True:
    if position == 1:
        if digit < 11:
            answer[0] = digit
            position += 1
            digit = 1
            #print("Position 1 found.")
            afound = True
        else:
            print("Position 1 cannot be greater than 11!")
            break
    if position == 2:
        if digit > 10:
            position -= 1
            digit = answer[0] + 1
            answer[0] = 0
        elif digit not in answer:
            answer[1] = digit
            position += 1
            digit = 1
            #print("Position 2 found.")
            bfound = True
        else:
            digit += 1
    if position == 3:
        if digit > 10:
            position -= 1
            digit = answer[1] + 1
            answer[1] = 0
        elif digit not in answer:
            answer[2] = digit
            position += 1
            digit = 1
            sums = (answer[0] + answer[1] + answer[2])
            #print("Position 3 found.")
            cfound = True
        else:
            digit += 1
    if position == 4:
        if digit > 10:
            position -= 1
            digit = answer[2] + 1
            answer[2] = 0
        elif digit not in answer:
            if(answer[2] + digit) < sums:
                answer[3] = digit
                position += 1
                digit += 1
                #print("Position 4 found.")
                dfound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 5:
        if digit > 10:
            position -= 1
            digit = answer[3] + 1
            answer[3] = 0
        elif digit not in answer:
            if (answer[2] + answer[3] + digit) == sums:
                answer[4] = digit
                position += 1
                digit += 1
                #print("Position 5 found.")
                efound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 6:
        if digit > 10:
            position -= 1
            digit = answer[4] + 1
            answer[4] = 0
        elif digit not in answer:
            if (answer[4] + digit) < sums:
                answer[5] = digit
                position += 1
                digit += 1
                #print("Position 6 found.")
                ffound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 7:
        if digit > 10:
            position -= 1
            digit = answer[5] + 1
            answer[5] = 0
        elif digit not in answer:
            if (answer[4] + answer[5] + digit) == sums:
                answer[6] = digit
                position += 1
                digit += 1
                #print("Position 7 found.")
                gfound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 8:
        if digit > 10:
            position -= 1
            digit = answer[6] + 1
            answer[6] = 0
        elif digit not in answer:
            if (answer[6] + digit) < sums:
                answer[7] = digit
                position += 1
                digit += 1
                print("Position 8 found: ", answer, " Sum: ", sums)
                hfound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 9:
        if digit > 10:
            position -= 1
            digit = answer[7] + 1
            answer[7] = 0
        elif digit not in answer:
            if (answer[6] + answer[7] + digit) == sums:
                answer[8] = digit
                position += 1
                digit += 1
                #print("Position 9 found.")
                ifound = True
            else:
                digit += 1
        else:
            digit += 1
    if position == 10:
        if digit > 10:
            position -= 1
            digit = answer[8] + 1
            answer[8] = 0
        if digit not in answer:
            if (answer[1] + answer[2] + digit) == sums:
                answer[9] = digit
                position += 1
                digit += 1
                #print("Position 10 found!!!!!!!!!!!!!!")
                jfound = True
                break
            else:
                digit += 1
        else:
            digit += 1
    #print(digit)
    #print(answer)

t2 = time.clock()
print(answer)
print(afound, bfound, cfound, dfound, efound, ffound, gfound, hfound, ifound, jfound)
print("Execution time: ", str(t2-t1)[:5])
            
