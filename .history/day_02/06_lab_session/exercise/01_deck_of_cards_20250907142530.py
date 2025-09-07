import random

def create_deck() -> list[str]:
	"""Return a list of 52 strings containing a standard deck"""
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def draw_top(deck: list[str], count: int = 1) -> list[str]:
	"""Remove and return count cards from the start of deck"""
	drawn = deck[:count]
	del deck[:count]
	return drawn

def draw_bottom(deck: list[str], count: int = 1) -> list[str]:
	"""Remove and return count cards from the end of the deck"""
	drawn = deck[-count:]
	del deck[-count:]
	return drawn

def draw_random(deck: list[str], count: int = 1) -> list[str]:
	"""Remove and return count random cards from the deck"""

def show(deck):
	"""TODO: Print all cards in deck"""

def add_top(deck: list[str], other: list[str]):
	"""TODO: Add cards in other to the first parts of deck"""

def add_bottom(deck: list[str], other: list[str]):
	"""TODO: Add cards in other to the last parts of deck"""

def add_random(deck: list[str], other: list[str]):
	"""Challenge: TODO: Add cards in other randomly to deck"""

def load(filename: str) -> list[str]:
	"""Challenge: TODO: Returns a list of cards loaded from a file"""

def save(deck: list[str], filename: str):
	"""Challenge: TODO: Saves a list of cards into a file (retrievable with load)"""
