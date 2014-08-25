# Problem 90: Cube digit pairs

class Dice(object):
	def __init__(self, left_die, right_die):
		self.left_die = left_die
		self.right_die = right_die

dice = Dice([0, 8], [1, 4])

class Stage(object):
	def __init__(self, die, next_obj, options):

		self.die = die
		self.next_obj = next_obj
		self.options = options
		self.generator = ([x for x in options])

	def go(self):

		for x in self.generator:
			self.die.append(x)
			if self.next_obj:
				self.next_obj.go()
			else: 
				print self.die
			self.die = self.die[:-1]

def main():
	stage3 = Stage(dice.left_die, None, range(1,10))
	stage2 = Stage(dice.left_die, stage3, [6, 9])
	stage1 = Stage(dice.left_die, stage2, [2, 5])
	stage1.go()



"""
	combinations = []

# Step 1: assign 2 or 5 to left[2]
	def step1():
		step1_options = [2,5]
		step1_generator = (x for x in step1_options)
		for x in step1_generator:
			dice['left'].append(x)
			step2()
			print x
			dice['left'] = dice['left'][:-1]

	def step2():
		print "step 2"
	step1()


# Step 2: assign 6 or 9 to left[3]
	step2_options = [6,9]
	step2_index = 0

	left[3] = step2_options[step2_index]
	step2_index += 1

# Step 3: assign one of range(9), not in left, to left[4]
	step3_options = [0,1,2,3,4,5,6,7,8,9]
	step3_index = 0

	while step3_options[step3_index] in left:
		step3_index += 1
	left[3] = step3_options[step3_index]
	step3_index += 1

# Step 4: assign one of range(9), not in left, to left[5]

# --

# Step 5: assign 2 or 5 to right[2], depending on left[2]

# Step 6: assign 6 or 9 to right[3]

# Step 7: assign one of range(9), not in right, to right[4]

# Step 8:
#   - If 3 not in left and 3 not in right, assign 3 to right[5]
#   - Else assign one of range(9), not in left, to right[5]"""

if __name__ == "__main__":
	main()
