# Combination Sum II
# Accepted 156 ms 172 (1st submit, 15 mins)
# KP: 
class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		re = []
		candidates.sort()
		re = self.sub(candidates,target)
		return re

	def sub(self,candidates,target):
		re = []
		for i in range(len(candidates)):
			if i >0 and candidates[i]==candidates[i-1]:
				continue
			if candidates[i] > target:
				break
			elif candidates[i] == target:
				re.append([candidates[i]])
				break
			else:
				for temp in self.sub(candidates[i+1:],target-candidates[i]):
					re.append([candidates[i]]+temp)
		return re

s = Solution()
n_input =[10,1,2,7,6,1,5]
re= s.combinationSum2(n_input,8)
for i in re:
	print i