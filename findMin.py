# Find Minimum in Rotated Sorted Array
# Accepted 140 ms 146 (1st submit, 30 mins)
# KP: Binary Search
# Can be improved as :  AL < AR then we could return AL
# Solution: https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
class Solution:
    # @param num, a list of integer
    # @return an integer
	def findMin(self, num):
		#### O(n)
		# last = num[-1]
		# for i in range(len(num)):
		# 	if num[i]<= last:
		# 		return num[i]
		###

		if len(num)==0:
			return None
		elif len(num)== 1:
			return num[0]
		elif len(num)==2:
			if num[0]>num[1]:
				return num[1]
			else:
				return num[0]
		else:
			mid = (len(num)-1)/2

			if num[0] < num[mid]:
				if num[0] < num[-1]:# Can be test first
					return num[0]
				else:
					return self.findMin(num[mid+1:])
			# elif num[0] = num[mid]:#0 = mid
			elif num[0]>num[mid]:
				return self.findMin(num[:mid+1])


		# return

s = Solution()
n_input =[4,5,6,7,0,1,2]
print s.findMin(n_input)