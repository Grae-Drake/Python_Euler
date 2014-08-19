# Problem 54: Poker Hands

import os

## Parse the text file.

raw_hands = 'TextFiles/poker.txt'
with open(raw_hands, 'r+') as my_file:
	games = [line.split() for line in my_file.readlines()]
print games[1][-1] # For testing the parse.


## Do objects

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
		

	# Methods to determine and set the possible hands.

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

	def pair_check(self, cards):
		twos = []
		for card in self.sorted_hand:
			if self.sorted_hand.count(card) == 2:
				twos.append(card)
		if len(set(twos)) == 1:
			return {'pair': True, 'pair': twos[0]}
		return{'pair': False}

	def highcard_check(self, cards):
		return self.sorted_hand
		
		
## Functions for manipulating hands

def sort_hand(cards):
	# Returns a sorted list of integers representing the hand
	translator = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
		'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}

	return sorted([translator[card[0]] for card in cards])

## Compare Hands