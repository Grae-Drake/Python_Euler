cards = ["Driaga", "Arthur", "Ashara", "Horus", "Cast"]
def perms(list, n): #takes all possible n elements from list
	if n == 0:
		return [[]]; #always forget that it's a list containing the empty list
	if len(list)<n:
		return []; #empty
	return [list[:1] + p for p in perms(list[1:],n-1)] + perms(list[1:],n)

for p in perms(cards, 3):
	print (p)
