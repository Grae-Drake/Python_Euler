def prime_sieve(limit):
    
        # create an empty start list and a counter
    start_list = []
    counter = 0
    root_limit = int(limit**.5 + 1)
    
        # populate the list with (limit-2) instances of "True"
        # remember that the list is not inclusive and we're ommitting 1
    for i in range(1,limit): 
        start_list.append(True)

        # flip the bits!
    for index1, value1 in enumerate(start_list):
        if (value1 == True) and (index1 > 1):
            for index2, value2 in enumerate(start_list):
                if index2 => index1**2:
                    value2 = False
                    
        else:
            pass

prime_sieve(10)
