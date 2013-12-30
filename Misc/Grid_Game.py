size = 3

grid = [[0]*size for item in range(size)]

prompt1 = [
    "Here is your grid.",
    "You start at the top left corner (at the 'X').",
    "Would you like to go down or right?"
    ]

prompt2 = [
    "Excelent!",
    "Let's do that again till we get to the bottom right corner!"
    ]

prompt3 = "Now, press 'D' for down and 'R' for right: "
        
move = 0

def print_grid():
    print("\n".join(" ".join(str(item) for item in row) for row in grid))
    
y_counter = 0
x_counter = 0

while y_counter < size-1 or x_counter <size-1:

    grid[y_counter][x_counter] = "X"
    
    if y_counter == 0 and x_counter == 0:
        print_grid()
        for item in prompt1:
            print(item)
            
    else:
        print_grid()
        for item in prompt2:
            print(item)
        
    while move == 0:
        
        command = input(prompt3).lower()
        
        if command == "d":
            move = "down"
        elif command == "r":
            move = "right"
        else:
            print("Oops, I didn't recognize that.")

        if move == "right":
            x_counter += 1
        else:
            y_counter += 1

    move = 0

grid[size-1][size-1] = "X"
print("\n".join(" ".join(str(item) for item in row) for row in grid))
print("Great job!")
        



