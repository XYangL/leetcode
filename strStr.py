# Implement strStr()
# Accepted 260 ms (2nd submit, 25 mins)
# KP: Both are ' '
class Solution:
	# @param haystack, a string
	# @param needle, a string
	# @return an integer
	def strStr(self, haystack, needle):
		ha_i = 0
		ne_i = 0

		if len(needle) == 0:#!!!
			return 0

		while ha_i != len(haystack):#!!!
			ha_ch = haystack[ha_i]
			ne_ch = needle[ne_i]
			if ha_ch == ne_ch:
				if ne_i == len(needle)-1:# find all sub
					return ha_i-ne_i
				else:# only find part, need to goon
					ha_i +=1
					ne_i +=1
			else:# not equal, neet to restart from ha_i-ne_i+1
				ha_i = ha_i-ne_i+1
				ne_i = 0

		return -1

s = Solution()
n_input ='thi'
sub = 'is'
print s.strStr(n_input,sub)
print n_input.find(sub)