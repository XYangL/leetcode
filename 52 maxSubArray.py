# Maximum Subarray
# Accepted 372 ms (1st submit)
class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		if len(A) == 1:
			# print A,' = max','\n'
			return A[0]
		# Find i : first index such that sum(A[0:i])<0
		pre_sum_max = A[0]
		pre_sum =0
		pre_index = len(A)
		for i in range(len(A)):
			pre_sum += A[i]
			if pre_sum < 0:
				pre_index = i
				break
			pre_sum_max = max([pre_sum_max,pre_sum])
			
		## not (every pre_sum >= 0 or i == len(S)-1 )
		if pre_index < len(A)-1:
			 pre_sum_max = self.maxSubArray(A[0:i+1])

		# Find j : first index such that sum(A[0:i])<0
		suf_sum_max = A[-1]
		suf_sum = 0
		suf_index = -1
		for j in range(len(A)-1, -1, -1):
			suf_sum += A[j]
			if suf_sum < 0:
				suf_index = j
				break
			suf_sum_max = max([suf_sum_max, suf_sum])
		
		## not (every suf_sum >= 0 or j == 0 )
		if suf_index > 0:
			 suf_sum_max = self.maxSubArray(A[j:])

		if pre_index < suf_index-1 :
			mid_sum_max = self.maxSubArray(A[pre_index+1:suf_index])
			# print A,'\n',i,j,'\n','max',[pre_sum_max, mid_sum_max,suf_sum_max],'\n'
			return max([pre_sum_max, mid_sum_max,suf_sum_max])
		else: # if i>=j, A[i+1,j] does not exist
			# print A,'\n',i,j,'\n','max',[pre_sum_max, suf_sum_max],'\n'
			return max([pre_sum_max, suf_sum_max])

s = Solution()
A = [-2,1,-3,4,-1,2,1,-5,4]#[1,1]#[-1,-1]#[-2,1,-3,4,-1,2,1,-5,4]
print range(len(A))
print A
print s.maxSubArray(A)
