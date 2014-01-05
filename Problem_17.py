num_list = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
    "Hundred",
    "Thousand",
    "And"]

zero = ["0"]

big_list = []

for item in range(1,1000):   # Populate list
    big_list.append(list(str(item)))

for item in big_list:       # Add leading zeros
    if len(item) == 1:
        item.insert(0,'') 
for item in big_list:
    if len(item) == 2:
        item.insert(0, '')
        
for item in big_list:       # replace index 1 with "XHundred"
    if item[0] == '1':
        item[0] = "OneHundred"      
for item in big_list:
    if item[0] == '2':
        item[0] = "TwoHundred"
for item in big_list:
    if item[0] == '3':
        item[0] = "ThreeHundred"
for item in big_list:
    if item[0] == '4':
        item[0] = "FourHundred"
for item in big_list:
    if item[0] == '5':
        item[0] = "FiveHundred"
for item in big_list:
    if item[0] == '6':
        item[0] = "SixHundred"
for item in big_list:
    if item[0] == '7':
        item[0] = "SevenHundred"
for item in big_list:
    if item[0] == '8':
        item[0] = "EightHundred"
for item in big_list:
    if item[0] == '9':
        item[0] = "NineHundred"
        
for item in big_list:
    if item[1] == '0' and item[2] == '0':  #insert 'And' where appropriate
        item.insert(1, '')
    else:
        item.insert(1, 'And')
for item in big_list:                   #remove 'And' where it was cropping up.
    if item[0] == '':
        item[1] = ''

for item in big_list:       # replace tens place with 'Twenty', etc.
    if item[2] == '2':
        item[2] = "Twenty"      
for item in big_list:       
    if item[2] == '3':
        item[2] = "Thirty" 
for item in big_list:       
    if item[2] == '4':
        item[2] = "Forty" 
for item in big_list:       
    if item[2] == '5':
        item[2] = "Fifty" 
for item in big_list:       
    if item[2] == '6':
        item[2] = "Sixty" 
for item in big_list:       
    if item[2] == '7':
        item[2] = "Seventy" 
for item in big_list:       
    if item[2] == '8':
        item[2] = "Eighty" 
for item in big_list:       
    if item[2] == '9':
        item[2] = "Ninety"

for item in big_list:       # Figure out them teens
    if item[2] == '0':
        item[2] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '0':
        item[2] = "Ten"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '1':
        item[2] = "Eleven"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '2':
        item[2] = "Twelve"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '3':
        item[2] = "Thirteen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '4':
        item[2] = "Fourteen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '5':
        item[2] = "Fifteen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '6':
        item[2] = "Sixteen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '7':
        item[2] = "Seventeen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '8':
        item[2] = "Eighteen"
        item[3] = ""
for item in big_list:       
    if item[2] == '1' and item[3] == '9':
        item[2] = "Nineteen"
        item[3] = ""

for item in big_list:       # Finally, on to the ones!    
    if item[3] == '0':      
        item[3] = "" 
for item in big_list:    
    if item[3] == '1':      
        item[3] = "One"      
for item in big_list:       
    if item[3] == '2':      
        item[3] = "Two"
for item in big_list:            

    if item[3] == '3':      
        item[3] = "Three"
for item in big_list:             
    if item[3] == '4':      
        item[3] = "Four"
for item in big_list:             
    if item[3] == '5':      
        item[3] = "Five"
for item in big_list:           
    if item[3] == '6':      
        item[3] = "Six"
for item in big_list:
    if item[3] == '7':      
        item[3] = "Seven"
for item in big_list:             
    if item[3] == '8':      
        item[3] = "Eight"
for item in big_list:          
    if item[3] == '9':      
        item[3] = "Nine"


step1_list = []

for item in big_list:
    step1_list.append(''.join(item))

step1_list.append('OneThousand')

bigstring = ''.join(step1_list)

answer = len(bigstring)

print(answer)
        
#import re           # this counts the instances of each word.

#for item in num_list:      
#    print(item, ', ',(re.subn(item, '', bigstring)[1]))






"""
Alternative manual count:

The numbers '1' through '9' show up 9 times per hundred. PLUS 100 times as a hundred-prefix
    Total: (9*10 + 100) = 190
    sum(1:9) = 36
The number '10' shows up 10 times per thousand
    Total: 10
    sum(10) = 3
The numbers '11' through '19' show up 1 time per hundred
    Total: (1*10) = 10
    sum(11:19) = 69
The numbers '10' through '90' (by tens) show up 10 times per hundred.
    Total: (10*10) = 100
    sum(20:90:10) = 47
The word 'hundred' shows up 900 times per thousand
    Total: 900
    sum(hundred) = 7
The word 'and' shows up whenever a hundred isn't exactly even
    Total: 891
    sum(and) = 3
The word thousand shows up once
    Total: 1
    sum(thousand) = 8

answer = (190*36 + 10*3 + 10*69 + 100*47 + 900*7 + 891*3 + 8)

print(answer)
"""

