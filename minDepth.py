# Minimum Depth of Binary Tree
# Accepted  376 ms ( 30 mins)
# KP: Determin Leaf; Root ?= None
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		if root == None:
			return 0 #!!!
		elif (root.left == None and root.right == None):
			return 1
		elif root.left == None:
			return self.minDepth(root.right)+1 #!!! +1 !!!
		elif root.right == None:
			return self.minDepth(root.left)+1 #!!! +1 !!!
		else:
			temp = min([self.minDepth(root.left), self.minDepth(root.right)])
			return temp+1

s = Solution()
n1l = TreeNode(2)
# n1l.left = TreeNode(4)
# n1l.right = TreeNode(5)

n1r = TreeNode(3)
# n1r.left = TreeNode(6)
n1r.right = TreeNode(7)

r = TreeNode(1)
r.left = n1l
r.right = n1r
n_input =r
print s.minDepth(n_input)