# Path Sum
# Accepted 312 ms (2st submit,  mins)
# KP: recursion
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
		has = False
		if root!=None:
			if not root.left and not root.right and root.val==sum:
				has = True
			else: #!!!
				if root.left!= None:
					has = self.hasPathSum(root.left, sum-root.val)
				if not has and root.right!=None: #!!!
					has = self.hasPathSum(root.right, sum-root.val)
	
		return has

n1l = TreeNode(4)
b = TreeNode(11)
b.left = TreeNode(7)
b.right = TreeNode(2)
n1l.left = b


n1r = TreeNode(8)
n1r.left = TreeNode(13)
a = TreeNode(4)
a.left = TreeNode(5)
a.right = TreeNode(1)
n1r.right = a

r = TreeNode(5)
r.left = n1l
r.right = n1r
#r = None
r = TreeNode(-2)
r.right = TreeNode(-3)

s = Solution()
n_input =r
print s.hasPathSum(n_input,-5)