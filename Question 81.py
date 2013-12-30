    # Problem 81: Path sum: two ways

f = open("matrix.txt")
grid = [map(int,item.split(",")) for item in f.readlines()]
f.close()

count = 1
grid_size = 80
diagonals = (grid_size * 2) - 2

while count <= diagonals :          
    # Evaluate diagonals, starting in the bottom right corner.
    # Rightmost value in diagonal is evaluated first, then move down and left.
    
    x_start = min(grid_size - 1, diagonals - count)
    y_start = max(grid_size - 1 - count, 0)
    x = x_start
    y = y_start
    while True:
        if y > grid_size - 1 or x < 0:
            count += 1
            break
        if x == grid_size - 1:
            grid[y][x] += grid[y+1][x]
        elif y == grid_size - 1:
            grid[y][x] += grid[y][x+1]
        else:
            grid[y][x] += min(grid[y+1][x], grid[y][x+1])
        x -= 1
        y += 1

print grid[0][0]
