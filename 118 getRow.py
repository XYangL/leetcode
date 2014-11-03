# Pascal's Triangle II
# Accepted 148 ms (1st Submit)
class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		if rowIndex <0:
			return []
		else:
			re = []
			return self.get_k(0,re,rowIndex)

	def get_k(self, n, num, k):
		num = [0]+num
		for i in range(n):
			num[i] += num[i+1]
		num[n]= 1
		if n == k:
			return num
		else:
			return self.get_k(n+1, num, k)

s = Solution()
print s.getRow(4)
