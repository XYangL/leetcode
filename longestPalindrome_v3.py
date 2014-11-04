# Longest Palindromic Substring
# Accepted 3196ms
# KP: Similar to DP
# KP: Construct Palindromic by Expanding from center
# KP: 2N-1 Kinds of Center
# O(N2) time and O(1) space
# http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

class Solution:
	def expand(self, s, l,r):
		n = len(s)
		while l>=0 and r<n and s[l]==s[r]:
			l -=1
			r +=1
		return s[l+1:r-1+1]

	# @return a string
	def longestPalindrome(self, s):
		n = len(s)
		if n == 0 :#!!!
			return ''
		longest = s[0]
		for i in range(n-1):# max(i) = n-2
			temp = self.expand(s, i,i)
			if len(temp)>len(longest):
				longest = temp
			temp = self.expand(s, i,i+1)
			if len(temp)>len(longest):
				longest = temp
		return longest


s = Solution()
n_input ="abbafaaccaa"
print s.longestPalindrome(n_input)