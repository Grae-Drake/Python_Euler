one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eightteen = 9
nineteen = 8
twenty = 6
thirty = 6
fourty = 6
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
thousand = 8
annd = 3 # Remember that biglist only goes up to 999 and that "and" is special

ones = one+two+three+four+five+six+seven+eight+nine
ones_frequency = 190
ones_total = ones*ones_frequency

tens_frequency = 10
tens_total = ten*tens_frequency

teens = eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eightteen+nineteen
teens_frequency = 10
teens_total = teens*teens_frequency

twenty_etc = twenty+thirty+fourty+fifty+sixty+seventy+eighty+ninety
twenty_etc_frequency = 100
twenty_etc_total = twenty_etc*twenty_etc_frequency

hundred_frequency = 900
hundred_total = hundred*hundred_frequency

and_frequency = 891
and_total = annd*and_frequency

thousand_total = thousand

answer = ones_total + tens_total + teens_total + twenty_etc_total + hundred_total + and_total + thousand_total


print(answer)






#big_list = []
#for item in range(1,100):
#    big_list.append(str(item))

#print(big_list)
