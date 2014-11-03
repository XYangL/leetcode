# Triangle
# Accepted 256 ms (1st submit, 25min)
class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		length = len(triangle)
		if length == 0:
			return 0
		elif length == 1:
			return triangle[0][0]
		else:
			for i in range(length-1,0,-1):
				for j in range(i):# i = len(triangle[i-1])
					triangle[i-1][j] = min([triangle[i][j]+triangle[i-1][j], triangle[i][j+1]+triangle[i-1][j]])
			return triangle[0][0]

		# return 

s = Solution()  
num = [[2]]#[[2],[3,4],[6,5,7],[4,1,8,3]]
print s.minimumTotal(num)