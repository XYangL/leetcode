# Longest Palindromic Substring
# ? Output Limit Exceeded [Imporved from v1]
# KP: Dynamic programming solution
#?? improve the above space complexit from O(N2) to O(N)
#?? p[][] to 3*p[]
# http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

class Solution:
	# @return a string
	def longestPalindrome(self, s):
		n = len(s)
		p = []
		maxStart = 0
		maxLen = 0
		
		p_2 = [True]*n
		p_1 = [False]*n

		maxLen = 1

		for i in range(n-1):
			if s[i]==s[i+1]:
				p_1[i] = True
				maxStart = i
				maxLen = 2
		print maxLen, '',''.join([str(i)+'  ' for i in p_1])

		for subLen in range(3,n+1):
			if maxLen < subLen -2:
				break
			else:
				p = [False]*n
				for i in range(n-subLen+1):# i +sublen-1 < len
					j = i+subLen-1
					if (s[i]==s[j]) and p_2[i+1]:# True
						p[i] = True
						maxStart = i
						maxLen = subLen
				p_2 = p_1
				p_1 = p		
				print maxLen, subLen,''.join([str(i)+'  ' for i in p])

		return s[maxStart:maxStart+maxLen]

s = Solution()
n_input ="aaabaa"
print s.longestPalindrome(n_input)