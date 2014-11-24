# Rotate Image
# Accepted 152 ms 20 (1st submit, 50 mins)
# KP: do this in-place
class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		n = len(matrix)
		if n>1:
			for dia in range(n/2):
				times = n-2*dia-1
				for t in range(times):
					new_row = dia
					new_col = dia+t
					temp = matrix[dia][dia+t]
					row = -1
					col = -1
					for r in range(3):
						col = new_row
						row = n-1-new_col
						matrix[new_row][new_col] =matrix[row][col] 
						new_row = row
						new_col = col

					matrix[new_row][new_col]= temp

		return matrix

s = Solution()
n_input =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in n_input:
	print i
re =s.rotate(n_input)
for i in re:
	print i