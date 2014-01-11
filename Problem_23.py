    # Problem 23: Non-abundant sums
    # Find the sum of all the positive integers which cannot be written
    # as the sum of two abundant numbers

    # Steps:
    #   First, list all abundant numbers up to 28123
    #   Second, figure out which numbers from 1-28123 are not the sum of
    #   any two abundant numbers.
    #   Third, sum those numbers.
import time, math

t0 = time.clock()

def calc_proper_factors(x):

    # Returns a list of proper factors of x
    proper_factors = sum([[y, x/y] for y in range(2,int(math.sqrt(x)+1)) if x % y == 0], [])
    proper_factors.append(1)
    return proper_factors

def list_abundant_nums(limit):

    # Returns a list of all abundant numbers below limit
    result = [x for x in range(1,limit+1) if x < sum(calc_proper_factors(x))]

    return result
    
def list_non_abundant_sums(limit):
    non_sums = []
    abundant_nums = list_abundant_nums(limit)
    found = False
    
    for number in range(1, limit):
        for i in range(len(abundant_nums)):
            for j in range(i, len(abundant_nums)):
                if abundant_nums[i] + abundant_nums[j] == number:
                    found = True
                elif abundant_nums[i] + abundant_nums[j] > number:
                    break
        if found == False:
            non_sums.append(number)
        found = False
    return non_sums
 
print calc_proper_factors(28)    
#print(list_non_abundant_sums(100))

t1 = time.clock()

print(t1-t0)

