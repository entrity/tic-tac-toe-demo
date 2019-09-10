import re

CELL_CODE_PATTERN = re.compile(r'^[A-Ca-c][1-3]$')
X = 1
O = -1
BLANK = 0
CHARS = {
	X: 'X',
	O: 'O',
	BLANK: '',
}

# Columns are A, B, C
# Rows are 1, 2, 3

class State(object):
	@staticmethod
	def decode_cell_code(cell_code):
		if not isinstance(cell_code, str):
			raise IllegalCellCodeException()
		if len(cell_code) != 2:
			raise IllegalCellCodeException()
		if not CELL_CODE_PATTERN.match(cell_code):
			raise IllegalCellCodeException()
		# `col` is {0,1,2}
		col = ord(cell_code[0].lower()) - ord('a')
		# `row` is {0,1,2}
		row = int(cell_code[1]) - 1
		# Return index into cells list
		return State.decode_row_col(row, col)

	@staticmethod
	def decode_row_col(row, col):
		if row < 0 or row > 2 or col < 0 or col > 2:
			raise IllegalCellCodeException()
		return 3 * row + col

	@staticmethod
	def decode(cell):
		if isinstance(cell, tuple):
			index = State.decode_row_col(*cell)
		else:
			index = State.decode_cell_code(cell)
		return index

	def __init__(self):
		self.cells = [BLANK for i in range(9)]

	# Return {'X', 'O', ''}
	def get_char(self, cell):
		value = self.get(cell)
		if value not in CHARS:
			raise IllegalStoredValueException()
		else:
			return CHARS[value]

	# Return {-1, 1, 0}
	def get(self, cell):
		return self.cells[State.decode(cell)]

	def set(self, cell, value):
		if value not in [X, O]:
			raise IllegalCellValueException()
		self.cells[State.decode(cell)] = value

	def pretty_print(self):
		print('%2s  A   B   C' % (''))
		print('%2s+---+---+---+' % (''))
		for r in range(3):
			print('%d | %1s | %1s | %1s |' % \
				(r+1, self.get_char((r,0)), self.get_char((r,1)), self.get_char((r,2))))
			print('%2s+---+---+---+' % (''))

	def get_winner(self):
		# check verticals
		for i in range(3):
			v = self.get((0,i))
			if v is BLANK: continue
			if v == self.get((1,i)) == self.get((2,i)): return v
		# check horizontals
		for i in range(3):
			v = self.get((i,0))
			if v is BLANK: continue
			if v == self.get((i,1)) == self.get((i,2)): return v
		# check diagonals
		v = self.get((1,1))
		if v is not BLANK:
			if v == self.get((0,0)) == self.get((2,2)): return v
			if v == self.get((0,2)) == self.get((2,0)): return v
		# no winner
		return BLANK

class IllegalCellCodeException(Exception):
	pass
class IllegalCellValueException(Exception):
	pass
class IllegalStoredValueException(Exception):
	pass

if __name__ == '__main__':
	state = State()
	state.pretty_print()
	print('winner', state.get_winner())
	state.set('A3', X)
	state.set('B1', O)
	state.set('C2', X)
	state.pretty_print()
	print('winner', state.get_winner())
	state.set('A1', X)
	print('winner', state.get_winner())
	state.set('A2', X)
	print('winner', state.get_winner())
	