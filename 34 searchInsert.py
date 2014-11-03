# Search Insert Position
# Accepted 148 ms (1st Submit)
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        else:
            for i in range(len(A)):
                if A[i] == target:
                    return i
                elif A[i] < target:
                    continue
                elif A[i] > target:
                    return i
            return len(A)
        