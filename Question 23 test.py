    # Problem 23: Non-abundant sums
    # Find the sum of all the positive integers which cannot be written
    # as the sum of two abundant numbers

    # Steps:
    #   First, list all abundant numbers up to 28123
    #   Second, figure out which numbers from 1-28123 are not the sum of
    #   any two abundant numbers.
    #   Third, sum those numbers.
import time
import math

t0 = time.clock()

def calc_proper_factors(x):
    proper_factors = []
    for item in range(2,int(math.sqrt(x)+1)):
        if x % item == 0:
            proper_factors.append(item)
            
            if int(x/item) not in proper_factors:
                proper_factors.append(int(x/item))
    proper_factors.append(1)
    return proper_factors

def list_abundant_nums(limit):
    big_list = [[item, 0] for item in range(1,limit+1)]
    for item in big_list:
        item[1] = sum(calc_proper_factors(item[0]))

    abundant_nums = []
    for item in big_list:
        if item[0] < item[1]:
            abundant_nums.append(item[0])
    return abundant_nums
    
def list_non_abundant_sums(limit):
    non_sums = []
    abundant_nums = list_abundant_nums(limit)
    found = False
    
    for number in range(1, limit):
        for i in range(len(abundant_nums)):
            if abundant_nums[i] <= (number/2):
                for j in range(i, len(abundant_nums)):
                    if abundant_nums[i] + abundant_nums[j] == number:
                        found = True
                    elif abundant_nums[i] + abundant_nums[j] > number:
                        break
            if found == True:
                break
        if found == False:
            non_sums.append(number)
        found = False
    return non_sums
    
list_non_abundant_sums(2000)

t1 = time.clock()

print(t1-t0)

