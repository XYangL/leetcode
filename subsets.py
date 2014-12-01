# Subsets
# Accepted 164 ms (1st submit,  mins)
# KP: Elements in a subset must be in non-descending order
# bin(): convert integer to bit string startting with '0b'
class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		S.sort()
		n = len(S)
		re = []
		for num in range(2**n):
			sub = []
			temp = bin(num)[2:]
			temp = '0'*(n-len(temp))+temp
			# print temp
			for i in range(n):
				if temp[i] =='1':
					sub.append(S[i])
			re.append(sub) 

		return	re

s = Solution()
n_input =[1,2,3]
print s.subsets(n_input)