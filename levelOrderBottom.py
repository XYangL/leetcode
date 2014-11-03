# Binary Tree Level Order Traversal II 
# Accepted 164 ms (2nd submit,  60 mins)
# KP: Leaf Node; reverse [::-1]
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if root == None:
			return []
		elif root.left == None or root.right == None:
			return self.levelOrderBottom(root.left)+self.levelOrderBottom(root.right)+[[root.val]]
		else:# left != None and right != None
			left = self.levelOrderBottom(root.left)[::-1]
			right = self.levelOrderBottom(root.right)[::-1]
			
			com = min([len(left),len(right)])
			result = [left[i]+right[i] for i in range(com)]
			
			if len(left) > len(right):
				result += left[com:] 
			elif len(right) > len(left):
				result += right[com:]
			
			result =[[root.val]]+result #!!!
			return result[::-1]

s = Solution()
n1l = TreeNode(9)
# n1l.left = TreeNode(4)
# n1l.right = TreeNode(5)

n1r = TreeNode(20)
n1r.left = TreeNode(15)
n1r.right = TreeNode(7)

r = TreeNode(3)
r.left = n1l
r.right = n1r
n_input =r
print s.levelOrderBottom(n_input)