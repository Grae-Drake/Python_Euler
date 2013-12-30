        # Call these functions by importing Euler_Fucntions, then
        # Euler_Functions.function()
        
def primeSieve(limit):
    array = [[x,True] for x in range(2,limit)]

    for x in array:
        value = x[0]
        primeness = x[1]
        for y in range((value)*2, limit, value):
            array[y-2][1] = False
    results = []
    for item in array:
        if item[1] == True:
            results.append(item[0])
    return results

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

def nextPrime(n):
    # Returns the smallest prime number larger than the argument
    testnum = n + 1
    answer = 0
    found = False
    while found == False:
        if isPrime(testnum) == True:
            answer = testnum
            found = True
        else:
            testnum += 1
    return answer


def previous_prime(n):
        # Returns the smallest prime number larger than the argument
    testnum = n + -1
    answer = 0
    found = False
    if n < 3:
        return "You can't go lower than 2!"
    else: 
        while found == False:
            if isPrime(testnum) == True:
                answer = testnum
                found = True
            else:
                testnum -= 1
        return answer

def is_palindrome(number):
    # Returns True if number is a palindrome.  Else returns False.

    number = str(number)
    result = True
    for index, item in enumerate(number):
        if index < math.ceil(len(number)/2):
            if number[index] != number[-1 - index]:
                result = False
    return result

def highest_common_factor(x,y):
    while x*y:
        if x > y:
            x %= y
        else:
            y %= x
    return max(x,y)

