# Find Peak Element
# Accepted 136 ms 57 (1st submit, 30 mins)
# KP: solution should be in logarithmic complexity.
# KP: Binary Search, Divide and Conquer?
class Solution:
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		l = len(num)
		if l==0:
			return -1
		elif l ==1:
			return 0
		elif l ==2:
			if num[0]>num[1]:
				return 0
			else:
				return 1
		else: # l>=3
			mid = l/2
			pre = num[mid-1]
			peak = num[mid]
			post = num[mid+1]

			# print pre, mid, peak
			if pre > peak:
				return self.findPeakElement(num[:mid])
			else: #pre<peak
				if peak >post:
					return mid
				else: #peak <post
					return mid+ self.findPeakElement(num[mid:])


s = Solution()
n_input = [1,2,3,4,3]
re = s.findPeakElement(n_input)
print 'num[',re,'] =' , n_input[re]