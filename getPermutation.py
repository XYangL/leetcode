# Permutation Sequence
# Accepted 144 ms
# KP: http://chaoren.is-programmer.com/posts/43994.html
# Let num = [1,2,3,...,n].
# The first digit is k/(n-1)!, then let k = k % (n-1)! and remove this digit from num. 
# The second digit is k/(n-2)!, then let k = k % (n-2)! and remove this digit from num and so on.
class Solution:
	# @return a string
	def getPermutation(self, n, k):
		re = ''
		num = range(1,n+1)
		k -= 1 #!!! count from 0 

		fact = 1
		for i in num[1:-1]:
			fact *=i

		while n!=1:
			cur = num[k/fact] 
			re +=str(cur)
			num.remove(cur)
			k %= fact			
			fact /= n-1
			n -=1
			
		re += str(num[0])
		return re

s = Solution()
n = 4
k = 6
print s.getPermutation(n,k)