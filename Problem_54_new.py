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
		self.flush = self.flush_check(cards)
		self.straight = self.straight_check(cards)
		self.four_kind = self.four_kind_check(cards)
		self.full_house = self.full_house_check(cards)
		self.three_kind = self.three_kind_check(cards)
		self.two_pair = self.two_pair_check(cards)
		self.pair = self.pair_check(cards)
		self.highcard = self.highcard_check(cards)
		self.sorted_hand = sort_hand(cards)

	# Methods to determine and set the possible xhands.

	def flush_check(self, cards):
		suit = cards[0][1]
		for card in cards:
			if card[1] != suit:
				return {'flush': False}
		return {'flush': True, 'sorted_hand': sort_hand(cards)}

	def straight_check(self, cards):
		pass

	def four_kind_check(self, cards):
		pass

	def full_house_check(self, cards):
		pass

	def three_kind_check(self, cards):
		pass

	def two_pair_check(self, cards):
		pass

	def pair_check(self, cards):
		pass

	def highcard_check(self, cards):
		pass

## Functions for manipulating hands

def sort_hand(cards):
	# Returnds a sorted list of integers representing the hand
	translator = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
		'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}

	return [translator[card[0]] for card in cards].sort()

## Compare Hands