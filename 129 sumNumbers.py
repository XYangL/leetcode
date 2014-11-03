# Sum Root to Leaf Numbers
# Accepted 132 ms
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def sumNumbers(self, root):
		if root == None:
			return 0 ;
		elif root.left == None and root.right == None:
			return root.val
		else:
			su = 0
			if root.left != None:
				root.left.val += root.val*10
				su += self.sumNumbers(root.left)
			if root.right != None:
				root.right.val += root.val*10
				su += self.sumNumbers(root.right)
			return su


s = Solution()
tn = TreeNode(0)
tn.left = TreeNode(1)
# tn.right = TreeNode(3)

print s.sumNumbers(tn)
