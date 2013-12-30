    # Problem 23: Non-abundant sums
    # Find the sum of all the positive integers which cannot be written
    # as the sum of two abundant numbers

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
    
def list_abundant_sums(limit):
    abundant_sums = []
    abundant_nums = list_abundant_nums(limit)
    found = False
    
    for i in range(len(abundant_nums)):
        for j in range(len(abundant_nums)):
            an_sum = abundant_nums[i] + abundant_nums[j]
            if (an_sum >= limit): break
            else: abundant_sums.append(an_sum)
    return abundant_sums

def sum_nonabundant_sums(limit):
    abundant_sums = list_abundant_sums(limit)
    nonabundant_sums = []
    for item in range(1,limit):
        if item not in abundant_sums:
            nonabundant_sums.append(item)
    answer = sum(nonabundant_sums)
    return answer
                    
    
print(sum_nonabundant_sums(28123))

t1 = time.clock()

print(t1-t0)

