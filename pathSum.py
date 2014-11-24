# Path Sum II
# Accepted 296 ms 114 (1st submit, 15 mins)
# KP: Recursive; Integer includes <=>0
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a list of lists of integers
	def pathSum(self, root, sum):
		re = []
		if root:
			re = self.add(root,sum)
		return re

	def add(self,root,sum):
		re = []
		if not root.left and not root.right:
			if root.val == sum:
				re.append([root.val])
		else:
			if root.left:
				re +=self.add(root.left,sum-root.val)
			if root.right:
				re +=self.add(root.right,sum-root.val)
			
			if len(re)!=0:
				for i in range(len(re)):
					re[i] = [root.val]+re[i]
		return re

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
s = Solution()
n_input =r
print s.pathSum(n_input,22)