# C limbing Stairs 
# Accepted 68 ms
class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		if n < 0:
			return 0
		elif n==0 or n==1 or n==2:
			return n
		else:
			step = [0]*n
			step[0]=1
			step[1]=2
			for i in range(2,n):
				step[i]=step[i-1]+step[i-2]
			return step[n-1]

s = Solution()
n = 4
print s.climbStairs(n)

'''
Status: Time Limit Exceeded
Last executed input:	35
'''
        