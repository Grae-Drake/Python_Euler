fibSec = [1,1]
counter = 0
term1 = 1
term2 = 1
while counter <=3524577:
        counter = term1+term2
        fibSec.append(counter)
        term1 = term2
        term2 = counter
evenFibSec = []
for i in fibSec:
        if i%2==0:
                evenFibSec.append(i)
total = sum(evenFibSec)
print(fibSec)
print (evenFibSec)
print(total)
