# Sort Colors
# Accepted 128 ms 86 (1st submit, 25 mins)
# KP: one-pass algorithm using only constant space
class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		pre = 0
		post = len(A)-1
		i = 0
		while i <= post:
			if A[i] ==0:
				A[pre]=0 #!!
				pre +=1
				i+=1
			elif A[i] ==1:
				i+=1
			elif A[i] ==2:
				A[i] = A[post]
				A[post] = 2
				post -=1

		for i in range(pre,post+1): #!!!
			A[i]=1
		return A

s = Solution()
n_input = [2,1,2,0,1,0,0,2,1,1,2,0,0,2,1]
print s.sortColors(n_input)