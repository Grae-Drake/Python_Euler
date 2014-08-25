# Problem 90: Cube digit pairs

import time

class Dice(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.combinations = []

dice = Dice([0, 8], [1, 4])

# Step 1: Append 2 or 5 to left[2]
def step1():
	step1_options = [2,5]
	step1_generator = (x for x in step1_options if x not in dice.left)
	for x in step1_generator:
		dice.left.append(x)
		step2()
		dice.left.pop()

# Step 2: Append one of range(10) (except for 0 and 8), not in left to left[3]
def step2():
	step2_options = [1,2,3,4,5,6,7,9]
	step2_generator = (x for x in step2_options if x not in dice.left)
	for x in step2_generator:
		dice.left.append(x)
		step3()
		dice.left.pop()

# Step 3: Append one of range(10) (except for 0 and 8), not in left, to left[4]
def step3():
	step3_options = [1,2,3,4,5,6,7,9]
	step3_generator = (x for x in step3_options if x not in dice.left)
	for x in step3_generator:
		dice.left.append(x)
		step4()
		dice.left.pop()

# Step 4: First, check to see if a 6 or 9 is needed (i.e, not all of 0,1,3, and4)
# If so, append 6 or 9.  Else, append one of range(10) (except for 0 and 8),
# not in left, to left[5]

def step4():
	prereqs = 0
	if 1 in dice.left:
		prereqs += 1
	if 3 in dice.left:
		prereqs += 1
	if 4 in dice.left:
		prereqs += 1
	if prereqs > 1:
		step4_options = [1,2,3,4,5,6,7,9]
	else:
		step4_options = [6,9]
	step4_generator = (x for x in step4_options if x not in dice.left)
	for x in step4_generator:
		dice.left.append(x)
		step5()
		dice.left.pop()

# Switch to right die

# Step 5: Append 2 or 5 to right[2], depending on left[2]
def step5():
	step5_options = [2,5]
	if 2 not in dice.left:
		dice.right.append(2)
		step6()
		dice.right.pop()
	if 5 not in dice.left:
		dice.right.append(5)
		step6()
		dice.right.pop()
	
	step5_generator = (x for x in step5_options if x not in dice.right)
	for x in step5_generator:
		dice.right.append(x)
		step6()
		dice.right.pop()

# Step 6: Append one of [6, 9], not in right, to right[3]
def step6():
	step6_options = [6,9]
	step6_generator = (x for x in step6_options if x not in dice.right)
	for x in step6_generator:
		dice.right.append(x)
		step7()
		dice.right.pop()

# Step 7: Append one of range(10) (except for 1, and 4), not in right, to right[4]
def step7():
	step7_options = [0,2,3,5,6,7,8,9]
	step7_generator = (x for x in step7_options if x not in dice.right)
	for x in step7_generator:
		dice.right.append(x)
		step8()
		dice.right.pop()

# Step 8:
#   - If 3 not in left and 3 not in right, assign 3 to right[5]
#   - Else assign one of range(10) (except for 1, 2, 3, 4, and 5), not in left, to right[5]"""
def step8():
	if 3 not in dice.left and 3 not in dice.right:
		dice.right.append(3)
		result = (tuple(sorted(dice.left)), tuple(sorted(dice.right)))
		dice.combinations.append(result)
		dice.right.pop()
	else:
		step8_options = [0,2,5,6,7,8,9]
		step8_generator = (x for x in step8_options if x not in dice.right)
		for x in step8_generator:
			dice.right.append(x)
			result = (tuple(sorted(dice.left)), tuple(sorted(dice.right)))
			dice.combinations.append(result)
			dice.right.pop()	

def main():
	step1()

if __name__ == "__main__":
	t1 = time.clock()
	main()
	answer = []
	for x in dice.combinations:
		if x not in answer and x[::-1] not in answer:
			answer.append(x)
	for x in answer:
		print x
	print len(answer)
	print "Execution time: {} seconds".format(time.clock() - t1)
