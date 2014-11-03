# Search a 2D Matrix
# Accepted 200 ms (1st Submit 20 mins)
class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		if len(matrix) == 0 or len(matrix[0])==0 or target < matrix[0][0]:
			return False
		else:
			for i in range(1,len(matrix)):
				if target < matrix[i][0]:
					try:
						matrix[i-1].index(target)
					except Exception, e:
						return False
					return True
				else:
					continue
			try:
				matrix[-1].index(target)
			except Exception, e:
				return False
			return True


	   

a = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]        
s = Solution()
print s.searchMatrix(a,16)