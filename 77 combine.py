# Combinations
# Accepted 272 ms (1st Submit 30 mins)
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
    	re = []
    	if n>0 and k>0 and k<=n:
    		if k == n:
    			re.append(range(1,n+1))
    		else:# k<n, n>=1, k>=1
    			re = self.get_comb(k,range(1,n+1))

    	return re

    # @param k, an integer
    # @param num, a list of integers
    # @return a list of lists of integers
    def get_comb(self, k, num):
    	if k == len(num):
    		return [num]
    	elif k == 1:
    		return [[i] for i in num]
    	else:
    		all_comb = []
    		for i in range(len(num)-k+1):
    			leader = [num[i]]
    			all_suf = self.get_comb(k-1,num[i+1:])
    			for suf in all_suf:
    				all_comb.append(leader+suf)
    		return all_comb

        

s = Solution()
n = 4
k = 2
print '\n'.join([str(i) for i in s.combine(n,k)])
