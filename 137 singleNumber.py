# Single Number II
# Accepted 232 ms
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	one = 0
    	two = 0
    	for i in A:
        	new_one = (i & ~one & ~two) |  (~i & one)
        	new_two = (i & one) | (~i & two)
        	
        	# new_one = (one^i)& ~two
        	# new_two = ()
        	one = new_one
        	two = new_two
        return one

s = Solution()
num = [2,3,3,2,2,1,3]
print s.singleNumber(num)
