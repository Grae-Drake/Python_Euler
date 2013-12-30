primes = [2]
counter = 3

while len(primes) <= 10000:
        if any(counter%x == 0 for x in primes):
                counter +=1
        else:
                primes.append(counter)
                counter +=1
                
        

print(primes[-1])
