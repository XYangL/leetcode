# Permutation Sequence
# Accepted 252 ms 200 (1st submit, 30 mins)
# KP: 
class Solution:
	# @return a string
	def getPermutation(self, n, k):
		
		return self.getFirst(range(1,n+1),k)

	def getFirst(self,num,k):
		fact = [1,1,2,6,24,120,720,5040,40320,362880]
		re = ''
		n = len(num)

		if k<=0:
			re = ''

		elif k ==1:
			re = ''.join([str(i) for i in num])

		elif k == fact[n]:
			re = ''.join([str(i) for i in num[::-1]])

		else:
			subs = fact[n-1]
			first = k/subs
			left = k%subs

			if left == 0:
				re = str(num[first-1])
				temp = num[:first-1]+num[first:]
				temp = ''.join([str(i) for i in temp[::-1]])
				# print num,k,re,temp,first
			else:
				re = str(num[first])
				temp = self.getFirst(num[:first]+num[first+1:],left)
			
			re +=temp
			# print num,k,re

		return re

s = Solution()
n = 4
k = 8
print s.getPermutation(n,k)