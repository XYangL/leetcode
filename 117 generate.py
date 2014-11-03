# Pascal's Triangle
# Accepted 180 ms
class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		tri = []
		if numRows > 0:
			for row_index in range(numRows):
				row = [1]
				for j in range(1,row_index):
					row.append(tri[row_index-1][j-1]+tri[row_index-1][j])
				if row_index>0 :
					row.append(1)
				tri += [row]
		return tri

s = Solution()		
n = 5
print s.generate(n)

        