# Problem 19: Counting Sundays

def createCalendar():
  """Returns a 3d list of 100 years of 12 months of 28-31 days."""

  calendar = {}
  months = [("January", 31),("February", 28),("March", 31),("April", 30),
  ("May", 31),("June", 30),("July", 31),("August", 31),("September", 30),
  ("October", 31),("November", 30),("December", 31)]
  yearCounter = 1901
  dayCounter = 1
  while yearCounter <= 1902:
    calendar[yearCounter] = {}
    for month in months:
      calendar[yearCounter][month[0]] = []
    yearCounter += 1
  return calendar

print(createCalendar())










#   # Initialize the calendar
#   calendar = [[[0]*30 for item in range(12)] for item in range(finalYear - startYear + 1)]

#   # Add a day to Jan, March, May, July, Aug, Oct and Dec,
#   # and remove two days from Feb.
#   monthCount = 1
#   for yearIndex, year in enumerate(calendar):
#     for monthIndex, month in enumerate(year):
#       if monthCount % 12 in [1,3,5,6,8,10,0]:
#         calendar[yearIndex][monthIndex].append([0])
#       elif monthCount % 12 == 2:
#         del calendar[yearIndex][monthIndex][0:2]
#       monthCount += 1

#   # Add a day to Feb in each leap year.
#   # Note: need to account for new generalized year solution.
#   for index, year in enumerate(calendar):
#     if (index) % 4 == 0:
#         year[1].append([0])

#   # Add a day counter and use it to fill the days of the months of the years of the calendar
#   day_count = 1                                   
#   for yearIndex, year in enumerate(calendar):        
#     for monthIndex, month in enumerate(year):
#       for dayIndex, day in enumerate(month):                       
#         calendar[yearIndex][monthIndex][dayIndex] = day_count % 7      
#         day_count += 1                                

#   return calendar

#     # Create a list of the first days of each month and populate it
# first_days = []
# for year_index, year in enumerate(calendar):        
#     for month_index, month in enumerate(year):
#         first_days.append(calendar[year_index][month_index][0])

#     # Count up all the Sundays.  Remember, Sundays are 0.
# answer = first_days.count(0)

# print(answer)
