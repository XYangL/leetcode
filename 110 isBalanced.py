# Balanced Binary Tree 
# Accepted 348 ms (1st Submit)
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		dep = self.depth(root)
		if dep == -1:
			return False
		else:
			return True

	def depth(self,root):
		if root == None:
			return 0
		else:
			left = self.depth(root.left)
			right = self.depth(root.right)

			if left == -1 or right == -1:
				return -1
			elif (left-right < 2) and (left-right > -2 ):
				return max([left,right])+1
			else:
				return -1
			if (left-right > 1) or (left-right < -1 ):
				return -1

n2l = TreeNode(2)
n2l.left = TreeNode(3)
# n2l.right = TreeNode(4)

n2r = TreeNode(2)
n2r.left = TreeNode(4)
n2r.right = TreeNode(3)

r = TreeNode(1)
# r.left = n2l
# r.right = n2r

s = Solution()
print s.isBalanced(r)
        