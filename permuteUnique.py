# Permutations II
# Accepted 388 ms (1st submit, 30 mins)
# KP: http://chaoren.is-programmer.com/posts/43020.html
class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		n = len(num)
		if n==0:#!!!
			re = []
		elif n==1:
			re = [num]
		else:
			re = []
			num.sort()
			for i in range(n):
				if i>0 and num[i]==num[i-1]:
					continue
				subs = self.permuteUnique(num[:i]+num[i+1:])
				for temp in subs:
					re.append([num[i]]+temp) #!!!
					# re.append(temp+[num[i]])

		return re

s = Solution()
n_input = [1,1,2]
print s.permuteUnique(n_input)