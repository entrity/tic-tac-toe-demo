#!/usr/bin/env python3

import sys, re
from state import State, X, O, BLANK
from state import IllegalCellCodeException, IllegalCellValueException, IllegalStoredValueException, CellOccupiedException
from game_tree import minimax

MAX_SEARCH_DEPTH = 9

def user_move(state, token):
	try:
		move = input('Where do you want to move? ')
		state.set(move, token)
		return True
	except IllegalCellCodeException:
		sys.stderr.write('Illegal format of input. All moves must be expressed as one of the letters {A,B,C} and one of the numerals {1,2,3} with no whitespace. E.g. A2\n')
		return False
	except CellOccupiedException:
		sys.stderr.write('Illegal move. That cell is already occupied.\n')
		return False

def computer_move(state, token):
	print('The computer is thinking. Please wait. (On my machine, this takes no more than 1 second.)')
	move = minimax(state, MAX_SEARCH_DEPTH, False)
	state.set(move, token)

def play_game(user):
	s = State()
	s.pretty_print()
	# Let computer play first if indicated
	if user == O:
		computer_move(s, -1*user)
		s.pretty_print()
	# Loop until end of game
	while not s.is_terminal():
		# User plays
		while not user_move(s, user):
			sys.stderr.write('Please try again.\n')
		s.pretty_print()
		if s.is_terminal(): break
		# Computer plays
		computer_move(s, -1*user)
		s.pretty_print()
	# Announce results
	winner = s.get_winner()
	sys.stdout.write('Winner: ')
	if winner == X:
		print('X')
	elif winner == O:
		print('O')
	else:
		print('tie')
	print('But really everyone\'s a winner because you both did your best.')

if __name__ == '__main__':
	# Prompt user for player token
	player_token = input('Which player do you want to be? X or O? ')
	while re.match(r'^[oOxX]$', player_token) is None:
		sys.stderr.write('Unfortunately, that is not a recognized option.\n')
		player_token = input('Which player do you want to be? X or O? ')
	if player_token in ('x', 'X'):
		player = X
		print('You get to move first')
	else:
		player = O
		print('\nThe computer gets to move first')

	play_game(player)
