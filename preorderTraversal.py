# Binary Tree Preorder Traversal
# Accepted 152 ms (2st submit, 20 mins)
# KP: Using stack for iterative solution
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
		stack = []
		vals = []
		if root != None:#!!!
			stack.append(root)
		
		while len(stack)>0:
			node = stack.pop()
			vals.append(node.val)
			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)
		
		return vals

s = Solution()
n1l = TreeNode(2)
n1l.left = TreeNode(4)
n1l.right = TreeNode(5)

n1r = TreeNode(3)
n1r.left = TreeNode(6)
n1r.right = TreeNode(7)

r = TreeNode(1)
r.left = n1l
r.right = n1r
n_input = r
print s.preorderTraversal(n_input)