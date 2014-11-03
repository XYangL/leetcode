# Single Number
# Accepted 296 ms
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = 0
        for i in A:
            ret ^= i
        return ret

s = Solution()
A = [1,2,3,4,3,2,1]

print s.singleNumber(A)