import pdb
import random, sys, math
from state import State, X, O, BLANK

def minimax(state, depth, is_seeking_max):
	if BLANK not in state.cells:
		raise Exception('minimax should not be called on a terminal state')
	if state.get_winner():
		raise Exception('minimax should not be called on a terminal state')
	if depth == 0:
		raise Exception('depth should not be 0 on first minimax call')
	if state.get_is_pristine():
		print('pristine')
		# Randomly choose between corners and center
		return random.choice([ State.decode(x) for x in ['A1','A3','B2','C1','C3']])
	else:
		score = _minimax_recursive(state, depth, is_seeking_max)
		return state.move

def _minimax_recursive(state, depth, is_seeking_max):
	# Handle terminal state
	winner = state.get_winner()
	if winner != BLANK:
		return winner * sys.maxsize
	# Recurse
	else:
		free_cells = state.get_free_cells()
		if len(free_cells) == 0:
			return 0
		random.shuffle(free_cells)
		# Recurse
		next_states = _get_next_states(state, free_cells, is_seeking_max)
		# for next_state in next_states: # todo delete
		# 	next_state.prev = state
		scores = [_minimax_recursive(s, depth-1, not is_seeking_max) for s in next_states]
		comparison_fn = max if is_seeking_max else min
		# Get best
		score, next_state, move = comparison_fn(list(zip(scores, next_states, free_cells)), key=lambda x: x[0]) # Remeber that each 'score' is a tuple of (score, choice)
		# state.next_state = next_state # todo delete
		# state.next_states = next_states # todo delete
		state.move = move
		if abs(score) > 999: score /= 2 # penalize slower victories
		return score

def _get_next_states(state, free_cells, is_seeking_max):
	cell_value = 1 if is_seeking_max else -1
	next_states = [state.clone() for x in free_cells]
	for i, cell in enumerate(free_cells):
		next_states[i].set(cell, cell_value)
	return next_states

def calc_score(state):
	working = 0
	def worth(triplet):
		if triplet[0] == triplet[1] == triplet[2]:
			return sys.maxsize * triplet[0]
		elif BLANK not in triplet:
			return 0
		else:
			return sum(triplet)*2
	# Horizontal
	for r in range(3):
		triplet = state.cells[r::3]
		working += worth(triplet)
	# Vertical
	for c in range(3):
		triplet = state.cells[c*3:(c+1)*3]
		working += worth(triplet)
	# Diagonal
	working += worth(state.cells[0::4]) # 0,4,8
	working += worth(state.cells[2:7:2]) # 2,4,6
	# Add points for corners and center
	working += sum(state.cells[0::2])
	# Return
	return working
