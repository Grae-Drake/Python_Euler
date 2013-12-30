
    # Create 3d list of 101 years of 12 months of 30 days
calendar = [[[0]*30 for item in range(12)] for item in range(101)]

    # Add a day Jan, March, May, July, Aug, Oct and Dec,
    # and remove two days from Feb
month_count = 1
for index1, year in enumerate(calendar):
    for index2, month in enumerate(year):
        if \
           month_count % 12 == 1 or \
           month_count % 12 == 3 or \
           month_count % 12 == 5 or \
           month_count % 12 == 7 or \
           month_count % 12 == 8 or \
           month_count % 12 == 10 or \
           month_count % 12 == 0:
            calendar[index1][index2].append([0])
        elif month_count % 12 == 2:
            del calendar[index1][index2][0:2]
        month_count += 1

    # Add a day to Feb in each leap year, then remove it from 1900
for index, year in enumerate(calendar):
    if (index)%4 == 0:
        year[1].append([0])
del calendar[0][1][0]

    # Add a day counter and use it to fill the days of the months of the years of the calendar
day_count = 1                                   
for year_index, year in enumerate(calendar):        
    for month_index, month in enumerate(year):
        for day_index, day in enumerate(month):                       
            calendar[year_index][month_index][day_index] = day_count % 7      
            day_count += 1                                

    # Remove the year first year (1900)
del calendar[0]

    # Create a list of the first days of each month and populate it
first_days = []
for year_index, year in enumerate(calendar):        
    for month_index, month in enumerate(year):
        first_days.append(calendar[year_index][month_index][0])

    # Count up all the Sundays.  Remember, Sundays are 0.
answer = first_days.count(0)

print(answer)
