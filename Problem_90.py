# Problem 90: Cube digit pairs

left = [0,8, None, None, None, None]
right = [1, 4, None, None, None, None]

# Step 1: assign 2 or 5 to left[2]

# Step 2: assign 6 or 9 to left[3]

# Step 3: assign one of range(9), not in left, to left[4]

# Step 4: assign one of range(9), not in left, to left[5]

# --

# Step 5: assign 2 or 5 to right[2], depending on left[2]

# Step 6: assign 6 or 9 to right[3]

# Step 7: assign one of range(9), not in right, to right[4]

# Step 8:
#   - If 3 not in left and 3 not in right, assign 3 to right[5]
#   - Else assign one of range(9), not in left, to right[5]
