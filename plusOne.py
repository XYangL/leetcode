# Plus One
# Accepted 228 ms (1st submit, 10 mins)
# KP: Overflow ?
class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		temp = ''.join([str(i) for i in digits])
		temp = int(temp)+1
		temp = [int(i) for i in str(temp)]
		return temp

s = Solution()
n_input =[1,2,3,4,9,9]
print s.plusOne(n_input)