def big_c_seq(limit):
    count = 1
    chain_lengths = []
    while count <= limit-1:
        chain_lengths.append([count, c_fun(count)])
        count += 1
    chain_lengths.sort(key=lambda x: x[1])
    print(chain_lengths[-1])
    

def c_fun(x):
    counter = 1
    var = x
    while var != 1:
        if var % 2 == 0:
            var = var/2
            counter += 1
        else:
            var = 3*var + 1
            counter += 1
           
    return counter


    
big_c_seq(1000000)
