# Longest Palindromic Substring
# Accepted 408ms
# KP: Manacher Algorithm
# Runs in O(N) time and O(N) space,
# Idea From: http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
# Self Note: https://www.evernote.com/shard/s142/nl/15380093/60e86236-3ef1-4250-86c1-54ffa87b6e6d/
class Solution:
	# @return a string
	def longestPalindrome(self, s):
		n = len(s)
		if n ==0 or n ==1:
			return s

		# 1. Transform S into T.
		# 	 For example, S = "abba", T = "^#a#b#b#a#$".
		# 	 ^ and $ signs are sentinels appended to each end to avoid bounds checking
		T = '^#'
		for i in range(n):
			T +=s[i]+'#'
		T +='$'
		n = len(T)
		# print T
		
		
		# 2. initial C, R, P
		C = 0
		R = 0
		P = [0]*n
		# print P
		
		# 3. for i in range(1:n-1)
		for i in range(1,n-1):
			i_mirror = 2*C-i
			
			# (R>i) ? min(R-i,p[j]) : 0
			if i < R:
				P[i] =  min([R-i,P[i_mirror]]) # 0 <= L< i_m
			else: 
				P[i] = 0 # include i=R

			# 4. Try to update P[i]
			# Attempt to expand palindrome centered at i
			while T[i+P[i]+1] == T[i-P[i]-1]:
				P[i] +=1


			# 5. Try Expand C and R
			# If palindrome centered at i expand past R,
			# adjust center based on expanded palindrome.
			if i+P[i] > R:
				R = i+P[i]
				C = i

		
		# 6 Find max p[i]
		centerI = 0
		maxLen = P[centerI]
		for i in range(1,n-1):
			if P[i]>maxLen:
				centerI = i
				maxLen = P[centerI]
		
		# print list(T)
		

		# 7 ouput sub
		start = (centerI - maxLen -1)/2
		return s[start:start+maxLen]# print P
		# print centerI, maxLen



s = Solution()
n_input ="aaccaaba"
print s.longestPalindrome(n_input)