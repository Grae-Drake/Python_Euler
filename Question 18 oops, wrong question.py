calendar = [[0]*365 for item in range(101)]     # Create 2d list with 101 years of 356 days

for index, item in enumerate(calendar):         # Add a day to each leap year
    if (index)%4 == 0:
        item.append([0])

del calendar[0][0]                              # Fix 1900 (not a leap year)

counter = 1                                     # Counter tracks the day of the week


for index1, item in enumerate(calendar):        # Loop through days of year and add integers
    for index2, element in enumerate(item):     # representing the day of the week.
        calendar[index1][index2] = counter % 7  # Monday is 1, Tuesday is 2, etc.,
        counter += 1                            # but remember that Sunday is 0.




del calendar[0]                                 # Remove the first year (1900)

januaries = []                                  # Create a list of januaries
for index, item in enumerate(calendar):         # Populate that list
    januaries.append(calendar[index][0:31])


first_january = calendar[0][0:31]


mondays = 0                                     # Create a counter for number of Mondays
for item in januaries:                          # Populate it!
    mondays += item.count(1)

januaries1 = januaries[0].count(1)
print(januaries[0])
print(januaries1)




#for index, item in enumerate(calendar):
#    print(len(item))






