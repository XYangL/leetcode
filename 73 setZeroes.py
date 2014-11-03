# Set Matrix Zeroes
# Accepted 608 ms
class Solution:
	# @param matrix, a list of lists of integers
	# RETURN NOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		m = len(matrix)
		if m != 0 :
			n = len(matrix[0])
			if n != 0:
				if self.product(matrix[0]) == 0:
					first_row = 0
				else:
					first_row = 1
				if self.product([matrix[i][0] for i in range(m)]) == 0:
					matrix[0][0] = 0


				for d in range(1,n):
					if self.product([matrix[i][d] for i in range(m)]) == 0:
						matrix[0][d] = 0
				for d in range(1,m):
					if self.product(matrix[d]) == 0:
						matrix[d][0] = 0

				for d in range(1,m):
					if matrix[d][0] == 0:
						matrix[d] = [0]*n
				for d in range(n):
					if matrix[0][d] == 0:
						for i in range(m):
							matrix[i][d] = 0

				if first_row == 0:
					matrix[0] = [0]*n

		return matrix

	def product(self, array):
	# only return 0 , will reset matrix;
	# or, if there is no 0, the matrix can not be kept as input
		for i in array:
			if i == 0:
				return 0
		return 1


s = Solution()
ma = [[0],[2],[3]]#[[0,0,0],[2,0,1],[3,3,3]]
print  '\n'.join([str(ma[i]) for i in range(len(ma))]),'\n'
ma = s.setZeroes(ma)
print  '\n'.join([str(ma[i]) for i in range(len(ma))])

'''
Input:	[[-1],[2],[3]]
Output:	[[1],[1],[1]]
Expected:	[[-1],[2],[3]]
'''
