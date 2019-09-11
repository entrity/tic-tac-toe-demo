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
			raise IllegalCellCodeException(cell_code)
		if len(cell_code) != 2:
			raise IllegalCellCodeException(cell_code)
		if not CELL_CODE_PATTERN.match(cell_code):
			raise IllegalCellCodeException(cell_code)
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
		if isinstance(cell, int) and cell >= 0 and cell <= 8:
			return cell
		elif isinstance(cell, tuple):
			index = State.decode_row_col(*cell)
		elif isinstance(cell, str):
			index = State.decode_cell_code(cell)
		else:
			raise IllegalCellCodeException(cell)
		return index

	def __init__(self):
		self.cells = [BLANK for i in range(9)]
		self.is_pristine = True

	def clone(self):
		other = State()
		other.cells = [value for value in self.cells]
		other.is_pristine = self.is_pristine
		return other

	def get_is_pristine(self):
		return self.is_pristine

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
		self.is_pristine = False

	def pretty_print(self):
		print('%2s  A   B   C' % (''))
		print('%2s+---+---+---+' % (''))
		for r in range(3):
			print('%d | %1s | %1s | %1s |' % \
				(r+1, self.get_char((r,0)), self.get_char((r,1)), self.get_char((r,2))))
			print('%2s+---+---+---+' % (''))

	# Return {-1, 1, 0}
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

	# Return an array of int to indicate unclaimed cells
	def get_free_cells(self):
		return [i for i,v in enumerate(self.cells) if v == BLANK]

	def __repr__(self):
		bldr = ''
		bldr += ('%2s  A   B   C\n' % (''))
		bldr += ('%2s+---+---+---+\n' % (''))
		for r in range(3):
			bldr += ('%d | %1s | %1s | %1s |\n' % \
				(r+1, self.get_char((r,0)), self.get_char((r,1)), self.get_char((r,2))))
			bldr += ('%2s+---+---+---+\n' % (''))
		return bldr

class IllegalCellCodeException(Exception):
	pass
class IllegalCellValueException(Exception):
	pass
class IllegalStoredValueException(Exception):
	pass

if __name__ == '__main__':
	state = State()
	state.pretty_print()
	print(state.get_free_cells())
	state.set('A3', X)
	state.set('B1', O)
	state.set('C2', X)
	state.pretty_print()
	print(state.get_free_cells())
