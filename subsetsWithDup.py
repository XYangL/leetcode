# Subsets II
# Accepted 224 ms 19 (2st submit, 20 mins)
# KP: http://yucoding.blogspot.hk/2013/05/leetcode-question-105-subsets-ii.html
# then generate new subsets ONLY from 
# the subsets generated from previous iteration, 
# other than the whole subsets list.
class Solution:
	# @param num, a list of integer
	# @return a list of lists of integer
	def subsetsWithDup(self, S):
		S.sort()
		re = [[]]
		n = len(S)
		re = [[]]
		for i in range(n):
			if i >0 and S[i]==S[i-1]:
				extend = new
			else:
				extend = re
			
			new = []
			for pre in extend:
				new.append(pre+[S[i]]) #!!! Elements in a subset must be in non-descending order.
			re +=new

		return re

s = Solution()
n_input =[1,2,3]
print s.subsetsWithDup(n_input)