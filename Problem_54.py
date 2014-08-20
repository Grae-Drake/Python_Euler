# Problem 54: Poker Hands

## Parse the text file.

raw_hands = 'TextFiles/poker.txt'
with open(raw_hands, 'r+') as my_file:
	games = [line.split() for line in my_file.readlines()]
print games[1] # For testing the parse.

## "Hand" class will contain attributes of a five card hand.
class Hand(object):

	# Create a hand object with a list of five cards.
	def __init__(self, cards):

		self.sorted_hand = sort_hand(cards)
		self.flush = self.flush_check(cards)
		self.straight = self.straight_check(cards)
		self.four_kind = self.four_kind_check(cards)
		self.full_house = self.full_house_check(cards)
		self.three_kind = self.three_kind_check(cards)
		self.two_pair = self.two_pair_check(cards)
		self.pair = self.pair_check(cards)
		self.highcard = self.highcard_check(cards)
		

	# Methods to evaluate attributes of hands.

	def show_hand(self):  # For testing
		print self.sorted_hand

	def flush_check(self, cards):
		suit = cards[0][1]
		for card in cards:
			if card[1] != suit:
				return {'flush': False}
		return {'flush': True, 'suit': suit}

	def straight_check(self, cards):
		for index, card in enumerate(self.sorted_hand[:-1]):
			if self.sorted_hand[index + 1] != card + 1:
				return {'straight': False}
		return {'straight': True, 'highest': self.sorted_hand[-1]}

	def four_kind_check(self, cards):
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 4:
				return {'four_kind': True, 'fours': card}
		return {'four_kind': False}

	def full_house_check(self, cards):
		threes = 0
		twos = 0
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 3:
				threes = card
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 2:
				twos = card
		if threes and twos:
			return {"full_house": True, "threes": threes, "twos": twos}
		else:
			return {"full_house": False}

	def three_kind_check(self, cards):
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 3:
				return {'three_kind': True, 'threes': card}
		return {'three_kind': False}

	def two_pair_check(self, cards):
		twos = []
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 2:
				twos.append(card)
		if len(set(twos)) == 2:
			return {'two_pair': True, 'pairs': sorted(set(twos))}
		return {'two_pair': False}

	def pair_check(self, cards):
		twos = []
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 2:
				twos.append(card)
		if len(set(twos)) == 1:
			return {'pair': True, 'pair_value': twos[0]}
		return{'pair': False}

	def highcard_check(self, cards):
		return self.sorted_hand
		

## Functions for manipulating hands

def sort_hand(cards):
	# Returns a sorted list of integers representing the hand. Disregards suit.
	translator = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
		'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}

	return sorted([translator[card[0]] for card in cards])

## Compare Hands

def did_p1_win(p1_hand, p2_hand):

	def compare_flush(p1_hand, p2_hand):

		p1_is_flush = p1_hand.flush['flush']
		p2_is_flush = p2_hand.flush['flush']
		if p1_is_flush == True and p2_is_flush == False:
			return True
		elif p1_is_flush == False and p2_is_flush == True:
			return False
		else:
			return compare_straight(p1_hand, p2_hand)

	def compare_straight(p1_hand, p2_hand):

		p1_is_straight = p1_hand.straight['straight']
		p2_is_straight = p2_hand.straight['straight']
		if p1_is_straight == True and p2_is_straight == False:
			return True
		elif p1_is_straight == False and p2_is_straight == True:
			return False
		elif p1_is_straight == True and p2_is_straight == True:
			return compare_highcard(p1_hand, p2_hand)
		else:
			return compare_four_kind(p1_hand, p2_hand)

	def compare_four_kind(p1_hand, p2_hand):

		p1_is_four_kind = p1_hand.four_kind['four_kind']
		p2_is_four_kind = p2_hand.four_kind['four_kind']

		if p1_is_four_kind == True and p2_is_four_kind == False:
			return True
		elif p1_is_four_kind == False and p2_is_four_kind == True:
			return False
		elif p1_is_four_kind == True and p2_is_four_kind == True:
			
			p1_fours = p1_hand.four_kind['fours']
			p2_fours = p2_hand.four_kind['fours']
			
			if p1_fours > p2_fours:
				return True
			elif p1_fours < p2_fours:
				return False
			else:
				return compare_highcard(p1_hand, p2_hand)
		else:
			return compare_full_house(p1_hand, p2_hand)

	def compare_full_house(p1_hand, p2_hand):

		p1_is_full_house = p1_hand.full_house['full_house']
		p2_is_full_house = p2_hand.full_house['full_house']

		if p1_is_full_house == True and p2_is_full_house == False:
			return True
		elif p1_is_full_house == False and p2_is_full_house == True:
			return False
		elif p1_is_full_house == True and p2_is_full_house == True:

			p1_threes = p1_hand.full_house['threes']
			p1_twoes = p1_hand.full_house['twoes']
			p2_threes = p2_hand.full_house['threes']
			p2_twoes = p2_hand.full_house['twoes']

			if p1_threes > p2_threes:
				return True
			elif p1_threes < p1_threes:
				return False
			elif p1_twoes > p2_twoes:
				return True
			elif p1_twoes < p2_twoes:
				return False
			else:
				print "Shit, you should never reach me.  Take me out!"

		else:
			return compare_three_kind(p1_hand, p2_hand)

	def compare_three_kind(p1_hand, p2_hand):

		p1_is_three_kind = p1_hand.three_kind['three_kind']
		p2_is_three_kind = p2_hand.three_kind['three_kind']

		if p1_is_three_kind == True and p2_is_three_kind == False:
			return True
		elif p1_is_three_kind == False and p2_is_three_kind == True:
			return False
		elif p1_is_three_kind == True and p2_is_three_kind == True:

			p1_threes = p1_hand.three_kind['threes']
			p2_threes = p1_hand.three_kind['threes']

			if p1_threes > p2_threes:
				return True
			elif p1_threes < p1_threes:
				return False
			else:
				return compare_highcard(p1_hand, p2_hand)

		else:
			return compare_two_pair(p1_hand, p2_hand)


	def compare_two_pair(p1_hand, p2_hand):

		p1_is_two_pair = p1_hand.two_pair['two_pair']
		p2_is_two_pair = p2_hand.two_pair['two_pair']

		if p1_is_two_pair == True and p2_is_two_pair == False:
			return True
		elif p1_is_two_pair == False and p2_is_two_pair == True:
			return False
		elif p1_is_two_pair == True and p2_is_two_pair == True:

			p1_pairs = p1_hand.three_kind['pairs']
			p2_pairs = p1_hand.three_kind['pairs']

			if p1_pairs[1] > p2_pairs[1]:
				return True
			elif p1_pairs[1] < p1_pairs[1]:
				return False
			if p1_pairs[0] > p2_pairs[0]:
				return True
			elif p1_pairs[0] < p2_pairs[0]:
				return False
			else:
				return compare_highcard(p1_hand, p2_hand)

		else:
			return compare_pair(p1_hand, p2_hand)

	def compare_pair(p1_hand, p2_hand):

		p1_is_pair = p1_hand.pair['pair']
		p2_is_pair = p2_hand.pair['pair']

		if p1_is_pair == True and p2_is_pair == False:
			return True
		elif p1_is_pair == False and p2_is_pair == True:
			return False
		elif p1_is_pair == True and p2_is_pair == True:

			p1_pair_value = p1_hand.pair['pair_value']
			p2_pair_value = p2_hand.pair['pair_value']

			if p1_pair_value > p2_pair_value:
				return True
			elif p1_pair_value < p2_pair_value:
				return False
			else:
				return compare_highcard(p1_hand, p2_hand)

		else:
			return compare_highcard(p1_hand, p2_hand)

	def compare_highcard(p1_hand, p2_hand):

		p1_high_to_low = sorted(p1_hand.sorted_hand, reverse=True)
		p2_high_to_low = sorted(p2_hand.sorted_hand, reverse=True)

		for x in range(5):
			if p1_high_to_low[x] > p2_high_to_low[x]:
				return True
			elif p1_high_to_low[x] < p2_high_to_low[x]:
				return False

	return compare_flush(p1_hand, p2_hand)

# Get down to business

def main():
	result = 0
	for game in games:
		p1_hand = Hand(game[:5])
		p2_hand = Hand(game[5:])
		if did_p1_win(p1_hand, p2_hand):
			result += 1
	return result

if __name__ == '__main__':
	print main()

