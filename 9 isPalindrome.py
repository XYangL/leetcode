# Palindrome Number
# Accepted 1888 ms
class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		re = False

		if x >=0 and x < 10:
			re = True
		elif x >= 10:

			length = 0
			y = x
			while y !=0:
				length +=1
				y = y/10

			factor = 10 ** (length -1)

			for i in range(length/2):
				if x/factor == x%10:
					x %= factor
					x /= 10
					factor /= 100
					re = True
				else:
					re = False
					break
		return re

a = 9
a = 11
# a = 121
a = 2147483647

s = Solution()
print s.isPalindrome(a)
        
'''
Status: Time Limit Exceeded
Last executed input:	2147483647

Input:	-2147483648
Output:	true
Expected:	false

Status: Time Limit Exceeded
Last executed input:	1955555591

Input:	121
Output:	false
Expected:	true

Input:	0
Output:	false
Expected:	true
'''

