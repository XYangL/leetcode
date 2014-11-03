# 4Sum
# Time Limit Exceeded
class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		num.sort()
		# print num
		# result = self.nSum(num, target, 4)
		# print '\n'.join([str(i) for i in result])
		return self.nSum(num, target, 4)

	def nSum(self, num, target, n):
		num_len = len(num)
		result = []
		if num_len<n:
			return []
		
		# len(num) > = n
		elif n == 1: # check if target in num[]
			for i in num:
				if i == target:
					result.append([i])
					break
			return result # if find, re = [[target]]; if not, re = []
			
		elif n >1:
			sub_list = self.nSum(num[1:], target-num[0], n-1)
			for sub in sub_list:
				result.append([num[0]]+sub)

			for i in range(1,num_len):
				if num[i-1] != num[i]:
					sub_list = self.nSum(num[i+1:], target-num[i], n-1)
					for sub in sub_list:
						result.append([num[i]]+sub)
		return result



S = [0,0,0,0]
target = 0

so = Solution()

aa = so.fourSum(S,target)
print aa
# print '\n'.join([str(i) for i in aa])