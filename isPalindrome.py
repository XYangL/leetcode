# Valid Palindrome
# Accepted  264 ms (2nd submit, 25mins)
# KP: String operation, lower case; alphanumeric  == alpha & digit
class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
	    
		s = ''.join(c for c in s if (c.isalpha() or c.isdigit()))
		s = s.lower()
		# print s
		half = len(s)/2
		pre = s[0:half]
		
		if len(s)%2 == 1:
			half +=1
		suf = s[len(s):half-1:-1]

		return pre == suf
        

s = Solution()
# n_input = 'A man, a plan, a canal: Panama'
n_input = '1a2'
print s.isPalindrome(n_input)
