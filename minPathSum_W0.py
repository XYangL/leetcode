# Minimum Path Sum
# Time Limit Exceeded
# KP: DP
class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		m = len(grid)
		if m == 0:
			return 0
		
		# m>=1
		else:
			n = len(grid[0])
			if n == 0:
				return 0
			
			# n>=1 & m>=1
			elif m == 1:
				return sum(grid[0])
			elif n == 1:
				return sum([i[0] for i in grid])
			
			# m>1 & n>1
			else:
				print grid[0][0]
				right = self.minPathSum([i[1:] for i in grid])
				down = self.minPathSum(grid[1:])
				return grid[0][0]+min([right,down])

		# return 0

s = Solution()
n_input = [[1,4,7],[2,5,8],[3,6,9]]#[[1,2,3],[4,5,6],[7,8,9]]
print s.minPathSum(n_input)