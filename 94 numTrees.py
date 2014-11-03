# Unique Binary Search Trees 
# Accepted 356 ms (1st submit)
class Solution:
    # @return an integer
    def numTrees(self, n):
    	if n <=0: 
    		return 0
    	elif n <=2: # n ==1 or n==2  
    		return n
    	else:
    		num = 0
    		for c in range(1,n+1):
    			l = self.numTrees(c-1)
    			r = self.numTrees(n-c)
    			# print c,l,r
    			if l *r == 0:
    				num += l+r
    			else:
    				num += l*r
    		return num

s = Solution()
print s.numTrees(3)
        