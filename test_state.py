# This is just a file of unit tests
from state import State, X, O, BLANK

def test_get_winner():
	# vertical
	s = State()
	assert s.get_winner() == BLANK, s.get_winner()
	s.set('A3', X)
	s.set('B1', O)
	s.set('C2', X)
	s.set('A2', X)
	assert s.get_winner() == BLANK, s.get_winner()
	s.set('A1', X)
	assert s.get_winner() == X, s.get_winner()
	# horizontal
	s = State()
	s.set('C2', O)
	s.set('C1', O)
	assert s.get_winner() == BLANK, s.get_winner()
	s.set('C3', O)
	assert s.get_winner() == O, s.get_winner()
	# diagonal
	s = State()
	s.set('A3', X)
	s.set('B2', X)
	s.set('B3', O)
	assert s.get_winner() == BLANK, s.get_winner()
	s.set('C1', X)
	assert s.get_winner() == X, s.get_winner()
	# dummy
	s = State()
	s.set('B2', O)
	s.set('B1', X)
	s.set('B3', O)
	assert s.get_winner() == BLANK, s.get_winner()

if __name__ == '__main__':
	test_get_winner()
