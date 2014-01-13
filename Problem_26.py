# Problem 26: Reciprical cycles

def get_recurring_cycle(numerator, denominator):

    # Returns the recurring cycle of the decimal representation of the quotient
    # of numerator / denominator.
    result = []
    r = numerator/denominator
    d = denominator * r
    result.append(r)
    print numerator%denominator

get_recurring_cycle(10,7)

"UGGGGGGGGGGGHG"
    