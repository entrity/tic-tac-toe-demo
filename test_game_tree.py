# This file does not raise exceptions when tests fail. These tests were used
# in an exploratory manner during development and can be used in the same
# manner during maintenance. However, these tests could be modified to raise
# exceptions on unexpected results. Be aware that there is some randomization
# in what moves the computer takes when presented with multiple equally good
# options, and that can affect the repeatability of some tests.

# Modify the code at the bottom of this file to determine which of the test
# functions get run.

# Usage:
# 	python3 test_game_tree.py

from state import State, X, O, BLANK
import game_tree

def test_score():
	s = State()
	s.set('A3', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('B1', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('C2', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('A2', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('A1', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s = State()
	s.set('C2', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('C1', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('C3', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s = State()
	s.set('A3', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('B2', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('B3', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('C1', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s = State()
	s.set('B2', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('B1', X)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s.set('B3', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))
	s = State()
	s.set('B2', O)
	s.set('B1', X)
	s.set('A2', O)
	s.pretty_print(); print('>> %d <<' % game_tree.score(s))

def test_minimax():
	# 1 move away from win
	s = State()
	print(s.get_is_pristine())
	s.set('B2', O)
	s.set('B1', X)
	s.set('A2', O)
	s.set('C1', X)
	s.pretty_print()
	ret = game_tree.minimax(s, 5, True)
	print(ret)
	# ret = game_tree.minimax(s, 5, True)
	# print(ret)

def test_cpu_vs_cpu_1_move():
	# X seeks max, O seeks min
	s = State()
	s.set('B1', X)
	s.set('B2', O)
	s.set('C1', X)
	s.set('A2', O)
	m = game_tree.minimax(s, 9, True)
	print('move', m)
	s.set(m, X)
	print(s)

def test_cpu_vs_cpu():
	s = State()
	s.set('A1', X)
	s.set('b2', O)
	s.set('c3', X)
	game_tree.minimax(s, 9, False)
	return
	# X seeks max, O seeks min
	s = State()
	print(s.get_is_pristine())
	for i in range(5):
		player = X if (i % 2 == 0) else O
		m = game_tree.minimax(s, 9, i % 2 == 0)
		if m is not None:
			s.set(m, player)
			score = game_tree.calc_score(s)
			print('move %d to %d player %2d score %d' % (i, m, player, score))
			print(s)


if __name__ == '__main__':
	# test_score()
	# test_minimax()
	test_cpu_vs_cpu()
