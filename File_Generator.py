import time
t1 = time.clock()

def primeSieve(limit):
    import time
    t1 = time.clock()
    array = [[x,True] for x in range(2,limit)]

    for x in array:
        value = x[0]
        primeness = x[1]
        for y in range((value)*2, limit, value):
            array[y-2][1] = False
    t2 = time.clock()
    print("Sieve time: " + str(t2 - t1))
    results = []
    for item in array:
        if item[1] == True:
            results.append(item[0])
    t3 = time.clock()
    print("List time: " + str(t3 - t2))
    return results

f = open('Sub_Million_Primes.txt', 'w+')

for item in primeSieve(1000000):
    f.write(str(item)+ ",")

f.close()

t3 = time.clock()
print("done")
