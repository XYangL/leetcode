# Symmetric Tree 
# Accepted 156 ms (1st Submit)
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		if root == None:
			return True
		else:
			return self.isSym(root.left, root.right)

	def isSym(self, left, right):
		if left == None and right == None:
			return True
		elif left != None and right != None:
			if left.val != right.val:
				return False
			else:
				le = self.isSym(left.left, right.right)
				ri = self.isSym(left.right, right.left)
				return (le and ri)
		else:# only of of left/right is None, l!=r
			return False


s = Solution()

n2l = TreeNode(2)
n2l.left = TreeNode(3)
n2l.right = TreeNode(4)

n2r = TreeNode(2)
n2r.left = TreeNode(4)
n2r.right = TreeNode(3)

r = TreeNode(1)
r.left = n2l
r.right = n2r

print s.isSymmetric(r)
        