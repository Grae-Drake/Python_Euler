    # Problem 68: Magic 5-gon ring

import time
t1 = time.clock()


answer = [0,0,0,0,0,0]
digit = 1
position = 0
sums = 0

while True:
    if digit > 6:
        if position == 0:
            print("Position 0 can't be greater than 6!")
            break
        else:
            digit = answer[position -1] + 1
            answer[position -1] = 0
            position -= 1
    elif digit not in answer:
        if position <= 2:
            answer[position] = digit
            digit = 1
            position += 1
        else:
            test = 0
            if position == 3:
                sums = (answer[0] + answer[1] + digit)
                test = sums
            elif position == 4:
                test = (answer[1] + answer[2] + digit)
            elif position == 5:
                test = (answer[2] + answer[0] + digit)
            if test == sums:
                answer[position] = digit
                if position < 5:
                    digit = 1
                    position += 1
                else:
                    print(answer)
                    print(answer[0], answer[1], answer[3], ", ", sums)
                    print(answer[1], answer[2], answer[4])
                    print(answer[2], answer[0], answer[5])
                    
                    if answer[2] != 6:
                        digit = 1
                        position = 3
                        answer[3] = answer[4] = answer[5] = 0
                        answer[2] += 1
                    else:
                        digit = 1
                        position = 2
                        answer[2] = answer[3] = answer[4] = answer[5] = 0
                        answer[1] += 1
            else:
                digit += 1
            
        
    else:
        digit += 1

        


        

t2 = time.clock()
print("Execution time: ", str(t2-t1)[:5])
