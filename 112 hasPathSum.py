# Path Sum
# Accepted 364 ms
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):    	
		# print str(root.val),sum ,'\t#1'
		if root == None:
			return False

		if (root.left == None and root.right == None): #leaf
			# print str(root.val) ,'\t#3'
			if sum - root.val == 0:
				return True
			if sum - root.val != 0:
				return False
		else:
			# print str(root.val),sum-root.val ,'\t#4'
			is_has = False
			if root.left !=None:
				is_has = self.hasPathSum(root.left, sum-root.val)

			if root.right !=None:
				is_has = is_has or self.hasPathSum(root.right, sum-root.val)
			
			return is_has

'''
Input:	{-2,#,-3}, -5
Output:	false
Expected:	true

Input:	{1,2}, 4
Output:	null
Expected:	false

Input:	{1}, 1
Output:	1
Expected:	true
'''