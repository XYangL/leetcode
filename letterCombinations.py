# Letter Combinations of a Phone Number
# Accepted 144 ms 25 (1st submit, 15 mins)
# KP: string to list : list(str)
class Solution:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):
		dic = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
		re = ['']
		# if len(digits)>0:
		# 	temp = dic[int(digits[-1])]
		# 	re = temp.split()
		for i in list(digits)[::-1]:
			chs = list(dic[int(i)])
			temp = []
			for ch in chs:
				for j in re:
					temp.append(ch+j)
			re = temp

		return re

s = Solution()
n_input ='23'
print s.letterCombinations(n_input)