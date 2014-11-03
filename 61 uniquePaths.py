# Unique Paths
# Accepted 164 ms
class Solution:
	# @return an integer
	def uniquePaths(self, m, n):
		if m <= 0 or n <= 0:
			return 0
		elif m ==1 or n ==1:
			return 1
		else:
			re = 1
			for i in range(1, m+n-1):
				re *= i
			for i in range(1,m):
				re /=i
			for i in range(1,n):
				re /=i
			return re

	def uniquePaths2(self, m, n):
		if m <= 0 or n <= 0:
			return 0
		elif m ==1 or n ==1:
			return 1
		else:
			down_num = self.uniquePaths(m-1,n)
			right_num = self.uniquePaths(m,n-1)
			return down_num+right_num


s = Solution()
m = 7
n = 3
print s.uniquePaths(m,n)
print s.uniquePaths2(m,n)
        
'''
Dynamic Programming
	def uniquePaths(self, m, n):
		if m <= 0 or n <= 0:
			return 0
		elif m ==1 or n ==1:
			return 1
		else:
			down_num = self.uniquePaths(m-1,n)
			right_num = self.uniquePaths(m,n-1)
			return down_num+right_num
'''