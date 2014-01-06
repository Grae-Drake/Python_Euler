    # Problem 18: Maximum path sum

import time
t1 = time.clock()

triangleFile = open("/Users/graedrake/Documents/Projects/Python_Euler/TextFiles/Problem18Data.txt")
triangle = [x.split() for x in triangleFile]
triangleFile.close()

def main(triangle):
    
    revisedTriangle = triangle[-2::-1]
    for i, row in enumerate(revisedTriangle):
        for j, element in enumerate(row):
            lowerElement0 = int(triangle[-(i+1)][j])
            lowerElement1 = int(triangle[-(i+1)][j+1])
            revisedTriangle[i][j] = int(element) + max(lowerElement0, lowerElement1)
    return revisedTriangle[-1][0]

print(main(triangle))
print "Execution time: " + str(time.clock() - t1) + " seconds."

