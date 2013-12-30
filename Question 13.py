grid = open("Problem_13_Grid.txt")

big_list = []
new_list = []

for line in grid:
    big_list.append(str(line))

for item in big_list:
    new_list.append(int(item.rstrip()))
    
answer = str(sum(new_list))

print(answer[:10])


