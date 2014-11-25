# Jump Game
# Accepted 220 ms 70 (1st submit, 25 mins)
# KP: Determine if both CURRENT and END are reachable 
# Idea From: http://blog.csdn.net/xiaozhuaixifu/article/details/13628465
class Solution:
	# @param A, a list of integers
	# @return a boolean
	def canJump(self, A):
		maxPos = 0

		end = len(A)
		for i in range(end):
			if i > maxPos:
				return False
			maxPos = max([maxPos,i+A[i]])
			if maxPos >= end-1:
				return True

s = Solution()
n_input =[3,2,1,0,4]#[2,3,1,1,4]
print s.canJump(n_input)