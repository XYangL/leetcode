# Longest Palindromic Substring
#  Time Limit Exceeded : "ccc ... ... ccc"
# KP: Dynamic programming solution
# Run time complexity of O(N2) and uses O(N2) space
# http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

class Solution:
	# @return a string
	def longestPalindrome(self, s):
		n = len(s)
		p = []
		maxStart = 0
		maxLen = 0
		for i in range(n):
			p += [[False]*n]

		for i in range(n):
			p[i][i] = True
		maxLen = 1

		for i in range(n-1):
			if s[i]==s[i+1]:
				p[i][i+1] = True
				maxStart = i
				maxLen = 2

		for subLen in range(3,n+1):
			for i in range(n-subLen-1):# i +sublen-1 < len
				j = i+subLen-1
				if (s[i]==s[j]) and p[i+1][j-1]:# True
					p[i][j] = True
					maxStart = i
					maxLen = subLen

		# for i in p:
		# 	print ''.join([str(j)+'\t' for j in i])

		return s[maxStart:maxStart+maxLen]

s = Solution()
n_input ="abadd"
print s.longestPalindrome(n_input)