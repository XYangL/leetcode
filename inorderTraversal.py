# Binary Tree Inorder Traversal
# Accepted 172 ms 67 (1st submit)
# KP: STACK; Interative
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		re = []
		stack = []
		while root!= None or len(stack)!=0:
			if root!= None:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				re.append(root.val)
				root = root.right
		return re

n1l = TreeNode('B')
n1l.left = TreeNode('D')

n1rl = TreeNode('E')
n1rl.left = TreeNode('G')
n1rl.right = TreeNode('H')

n1rr = TreeNode('F')
n1rr.right = TreeNode('I')

n1r = TreeNode('C')
n1r.left = n1rl
n1r.right = n1rr

r = TreeNode('A')
r.left = n1l
r.right = n1r
s = Solution()
n_input =r
print s.inorderTraversal(n_input)