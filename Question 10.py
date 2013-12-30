def prime_sieve(limit):
    
        # create an empty start list, an empty list of primes, and a counter
    start_list = []
    counter = 0
    root_limit = int(limit**.5 + 1)
    
        # populate the list with (limit-1) instances of "True"
    for i in range(1,limit): 
        start_list.append(True)
    print("I'm done making the list!")

         # flip the boolians with composite index numbers to "False"
    for index, item in enumerate(start_list[:root_limit], start=2):
        if start_list[index] == True:
            for i in range(1,(int(len(start_list)/(index)))):
                start_list[index*i-2] = False
                

        # start adding up the primes
    for index, item in enumerate(start_list, start=2):
        if item == True:
            counter += index
 
    print(start_list)

prime_sieve(11)



    
    
""" #starting definitions ***first try
    start_list = []
    primes = [2,3,5,7]
    
        # Create a starting list to sieve
    for i in range(4,limit+1): 
        if (i % 6 == 1 or i % 6 ==5) and (i % 5 != 0 and i % 7 != 0):
            start_list.append([i, False])
            
        # Flip non-primes to true
    for i in start_list:
        for x in start_list:
            if i[0] != x[0] and x[0] % i[0] == 0:
                x[1] = True
                
        # Put the primes into a list
    for i in start_list:
        if i[1] == False:
            primes.append(i[0])

    print(sum(primes))

prime_sieve(2000000)"""
