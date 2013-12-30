def calc_trig_num(x):
        # This helper function calculates the x-th triangle number
    triangle_number = 0
    tcount = x
    while tcount > 0:
        triangle_number += tcount
        tcount -= 1
    return triangle_number

def calc_factors(x):
        # This helper function lists out each of the factors
        # of a triangle number
    factors = []
    for i in range(1, int(int(x)**.5)):
        if x % i == 0:
            factors.append(i)
            factors.append(x/i)
    factors.sort()
    return len(factors)

def lowest_trig_num(n):
    
        # We calculate successively larger triangle numbers,
        # untile we reach the required number of factors
    num_of_factors = 0
    count = 0
    while num_of_factors <= n:
        count += 1
        triangle_number = calc_trig_num(count)
        num_of_factors = calc_factors(triangle_number)
        
    return(triangle_number)


print(lowest_trig_num(500))
        
