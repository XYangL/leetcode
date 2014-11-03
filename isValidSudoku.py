# Valid Sudoku
# Accepted 288 ms (3rd submit, 36 mins)
# KP: Hash Table; Need 3 more 2D array for each line, column and sub_box
# KP: Compute the index in the 2D array of sub_box
# Note: A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated
class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		copy1 = []
		copy2 = []
		copy3 = []
		for i in range(9):
			line = ['']*9
			copy1 += [line]
		for i in range(9):
			line = ['']*9
			copy2 += [line]
		for i in range(9):
			line = ['']*9
			copy3 += [line]


		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num!='.':
					num = int(num)
					box_i = (i/3)*3+(num-1)/3
					box_j = (j/3)*3+(num-1)%3 #!!!
					if (copy1[i][num-1]!='')or(copy2[num-1][j]!='')or(copy3[box_i][box_j]!=''):
						return False
					else:
						copy1[i][num-1] = num
						copy2[num-1][j] = num
						copy3[box_i][box_j] = num
        
		return True

s = Solution()
n_input = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]#array
print s.isValidSudoku(n_input)
# for i in array:
# 	print i