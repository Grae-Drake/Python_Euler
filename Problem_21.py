    # Problem 21: Amicable numbers

def proper_factors(n):

    # Returns a list of n's proper factors
    proper_factors = [1]
    for number in range(2,int(n**.5)+1):
        if n % number == 0:
            proper_factors.append(number)
            proper_factors.append(n/number)
    return proper_factors

def number_factor_sum_pairs(limit):
    
    # Create and return a dictionary with keys from 1 to limit and corresponding
    # values equal to the sum of the proper factors of the key.
    big_list = {}
    for n in range(1, limit):
        if n!= sum(proper_factors(n)):
            big_list[n] = sum(proper_factors(n))
    return big_list

def amicable_numbers(limit):

    # Returns a list of amicable numbers below limit
    result = []
    my_dict = number_factor_sum_pairs(limit)
    for key in my_dict:
        value = my_dict[key]
        if value in my_dict.keys() and my_dict[value] == key:
            result.append(key)
            result.append(value)
    return set(result)
    
print(sum(amicable_numbers(10000)))

