# Palindrome Number
# Status: Time Limit Exceeded
# Submitted: 0 minutes ago
# Last executed input:	2147483647
class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		re = False

		if x >= 0:
			length = 1
			y = x
			while y !=0:
				length +=1
				y = y/10

			if length == 1:
				re = True
			else:
				for i in range(length/2):
					left = length - 2*i -1
					print x/(10 ** left), x%10
					if x/(10 ** left) == x%10:
						re = True
					else:
						re = False
						break
		return re

a = 9
a = 11
a = 311

s = Solution()
print s.isPalindrome(0)
        
