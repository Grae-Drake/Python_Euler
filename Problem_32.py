        # Problem 29: Pandigital Products

def panCheck(*numbers):
    # Accepts an arbitrary amount of numbers as arguments and
    # returns True if the set of numbers is pandigital
    startList = []
    for item in numbers:
        item = str(item)
        for i in item:
            startList.append(i)
    startList.sort()
    endList = []
    lookup = []
    for item in startList:
        if item not in lookup:
            endList.append(item)
            lookup.append(item)
    if startList == endList:
        return True
    if startList != endList:
        return False

def zeroCheck(number):
    # Returns True if zero is not a digit in a number.
    startList = []
    lookup = []
    number = str(number)
    for item in number:
        if item not in lookup:
            startList.append(item)
            lookup.append(item)
    if '0' not in startList:
        return True
    else:
        return False

def nineCheck(x, y, product):
    x = str(x)
    y = str(y)
    product = str(product)
    test = x+y+product
    if len(test) == 9:
        return True
    else:
        return False
    
# First, let's build a list of pandigital factors        
factors = []
for x in range(8000):
    if zeroCheck(x) == True:
        if panCheck(x) == True:
            factors.append(x)

# Now that we have factors, let's multiply!

pandigitals = []
for x in factors:
    for y in factors:
        if panCheck(x, y) == True:
            product = x * y
            if zeroCheck(product) == True:
                if product > 1000:
                   if product <10000:
                       if nineCheck(x, y, product) == True:
                            if panCheck(x, y, product) == True:
                                pandigitals.append([x, y, product])

print(pandigitals)
products = []
counter = 0
for item in pandigitals:
    if item[2] not in products:
        products.append(item[2])
        counter += item[2]

print(counter)


        



