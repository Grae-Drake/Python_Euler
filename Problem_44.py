        # Problem 44: Pentagon Numbers
import math

pns = [int(x*(x*3 - 1)/2) for x in range(1,4000)]
answers = []

def pentagon(x):
    y = (math.sqrt(24*x+1)+1)/6
    if y.is_integer():
        return True
    else:
        return False
    
for x in pns:
    for y in pns:
        if pentagon(x+y) == True:
            if pentagon(abs(x-y)) == True:
                answers.append([x,y])
        
print(answers)
