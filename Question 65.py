    #Problem 64: Convergents of e

import time

t1 = time.clock()
def problem_64(terms):
    # Returns the sum of the digits of the numerator of the 100th
    # convergent of the continuing fraction for e
    
    sequence = [2]                      # Initialize the continuing fraction
    for x in range(1,(terms//3)+1):     # Add remaining values to con fract
        sequence.append(1)
        sequence.append(x*2)
        sequence.append(1)
    sequence = sequence[:terms]         # Cut the list down to size
    sequence[-1] = [sequence[-1],1]     # Convert the final value to a fraction
    while len(sequence) > 1:            # Roll up the values in reverse order
        z = sequence.pop()
        y = sequence.pop()
        z = list(reversed(z))
        z[0] += y * z[1]
        sequence.append(z)

    answer = sum([int(x) for x in str(sequence[0][0])])
    return(answer)

print(problem_64(100))
    
t2 = time.clock()

print("Execution time: ", t2-t1)


