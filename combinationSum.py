# Combination Sum 
# Accepted 384 ms 168 (2nd submit, 20 mins)
# KP: candidates canbe duplicated
# Special case: 1 is candidadates, then target - 1*n ==0
class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum(self, candidates, target):
		re = []
		candidates.sort()
		re = self.sub(candidates,target)
		return re

	def sub(self,candidates,target):
		re = []

		for i in range(len(candidates)):
			if i>0 and candidates[i]== candidates[i-1]:
				continue
			elif candidates[i] == target:
				re.append([candidates[i]])
			elif candidates[i]>target:
				break
			else:
				num = 1
				j = i+1
				while j<len(candidates) and  candidates[j]==candidates[i]:
					j = j+1
				while target-candidates[i]*num >0:
					for temp in self.sub(candidates[j:],target-candidates[i]*num):
						re.append([candidates[i]]*num+temp)
					num +=1
				
				if target-candidates[i]*num==0:#!!!
					re.append([candidates[i]]*num)
		return re

s = Solution()
n_input =[1,2,3,6,7]
print s.combinationSum(n_input,7)