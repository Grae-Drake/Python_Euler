    # Find the product of the digits of 100!

def fact_dig_product(x):
        #This function returns the product of the digits of x!
    counter = x
    factorial = 1
    while counter > 1:
        factorial *= counter
        counter -= 1
    fact_str = str(factorial)
    fact_list = []
    for item in fact_str:
        fact_list.append(int(item))
    answer = sum(fact_list)
    return answer

print(fact_dig_product(100))
