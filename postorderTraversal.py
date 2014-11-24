# Binary Tree Postorder Traversal
# Accepted 172 ms 67
# KP: how to determine all its children has been popped
# stack[-1].right == popped
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		re = []
		stack = []
		popped = None
		while root!= None or len(stack)!=0:
			if root!=None:
				stack.append(root)
				root = root.left
			elif stack[-1].right != popped:
				root = stack[-1].right
				popped = None
			else:# stack[-1].right == popped means
			# last stack node's right child has been just popped,
			# so all its children have been handled
			# it is time to pop itself
				popped = stack.pop()
				re.append(popped.val)

		return re



n1l = TreeNode(2)
n1l.left = TreeNode(4)
n1l.right = TreeNode(5)

n1r = TreeNode(3)
# n1r.left = TreeNode(6)
# n1r.right = TreeNode(7)

r = TreeNode(1)
r.left = n1l
r.right = n1r
#r = None	
s = Solution()
n_input =r
print s.postorderTraversal(n_input)