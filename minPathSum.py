# Minimum Path Sum
# Accepted 280 ms 61 ( 60 mins)
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
				p = []
				for i in range(m):
					p.append([0]*n)

				for i in range(m):
					for j in range(n):
						if i == 0:
							if j == 0:
								p[0][0]= grid[i][j]
							else:# i==0 j!=0 1st row
								p[0][j]= p[0][j-1]+grid[i][j]
						elif j==0:# i!=0 1st col
							p[i][0] = p[i-1][0]+grid[i][j]
						else:# i>=1, j>=1
							p[i][j] = min([p[i][j-1],p[i-1][j]])+grid[i][j]
				return p[m-1][n-1]


s = Solution()
n_input = [[1,2,3],[4,5,6],[7,8,9]]#[[1,4,7],[2,5,8],[3,6,9]]#[[1,2,3],[4,5,6],[7,8,9]]
print s.minPathSum(n_input)