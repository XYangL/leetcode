# Minimum Path Sum
# Accepted 312 ms 61 ( 60 mins)
# Improved Space Complexity = O(n)
# KP: Dynamic Programming ; dp[i][j] = grid[i][j] + min( dp[i-1][j], dp[i][j-1] );
# http://www.cnblogs.com/TenosDoIt/p/3774804.html
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
				s = 0
				for i in grid:
					s +=i[0]
				return s
			
			# m>1 & n>1
			else:
				p = [0]*n

				p[0] = grid[0][0]
				for j in range(1,n):
					p[j] = p[j-1]+grid[0][j]

				i = 1
				while i < m:
					p[0] += grid[i][0]
					for j in range(1,n):
						p[j] = min([p[j-1],p[j]])+grid[i][j]
					i +=1 #!!!
				
				return p[-1]


s = Solution()
n_input = [[1,2,3],[4,5,6],[7,8,9]]#[[1,4,7],[2,5,8],[3,6,9]]#[[1,2,3],[4,5,6],[7,8,9]]
print s.minPathSum(n_input)