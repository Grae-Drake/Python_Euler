    # Problem 82: Path sum: three ways

grid = [[131, 673, 234, 103, 18],[201,96,342,965,150],[630,803,746,422,111],
        [537,699,497,121,956],[805,732,524,37,331]]

def check_up(y,x):
    # Returns the cheapest path above the cell in grid given by the
    # y and x coordinates. The top left corner of the grid is 0,0.

    candidates = []
    vert = 0
    for i in range(1, y+1):
        up = grid[y-i][x]
        right = grid[y-i][x+1]
        vert += up
        candidates.append(vert + right)
    return min(candidates)

def check_down(y,x):
    # Returns the cheapest path below the cell in grid given by the
    # y and x coordinates. The top left corner of the grid is 0,0.

    candidates = []
    vert = 0
    for i in range(1, grid_size-y):
        down = grid[y+i][x]
        right = grid[y+i][x+1]
        vert += down
        candidates.append(vert + right)
    return min(candidates)
    
count = 2
grid_size = 5

while count <= grid_size :
    # Evaluate columns, starting second from the right.
    # Top value in column is evaluated first, then move down, but
    # order is not important.
    
    x = grid_size - count
    y = 0
    new_column = []
    while y < grid_size:
        if y == 0:
            new_column.append(grid[y][x] + min(check_down(y,x), grid[y][x+1]))
        elif y == grid_size - 1:
            new_column.append(grid[y][x] + min(check_up(y,x), grid[y][x+1]))
        else:
            new_column.append(
                grid[y][x] + min(check_down(y,x), check_up(y,x), grid[y][x+1]))
        y += 1

    # Now let's paste in the new column.
    #print(new_column)
    count2 = 0
    for item in new_column:
        grid[count2][x] = item
        count2 += 1

    count += 1

print min([row[0] for row in grid])

    


