range_100 = []

for i in range(1,101):
        range_100.append(i)

range_100_squares = []

for i in range_100:
        range_100_squares.append(i**2)

sum_of_squares = sum(range_100_squares)

square_of_sum = (sum(range_100))**2

answer = sum_of_squares - square_of_sum

print(answer)
