# Permutations
# Accepted 276 ms (1st submit, 20 mins)
class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		length = len(num)
		if length == 0:
			return []
		elif length == 1:
			return [num]
		else:
			re = []
			num.sort()
			# print num
			for i in range(length):
				if (i == 0) or (num[i] !=num[i-1]):
					subs = self.permute(num[0:i]+num[i+1:length])
					if subs == []:
						re.append([num[i]])
					else:
						for sub in subs:
							re.append([num[i]]+sub)
			return re

s = Solution()
num =[1,1,2] #[1,2,3]
print '\n'.join([str(i) for i in s.permute(num)])

        