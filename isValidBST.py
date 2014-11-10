# Validate Binary Search Tree
# Accepted 252 ms 56 cases (2 hours)
# KP: Simulate the generate way
# Left child should between left limit and root.val
# Right child should between right limit and root.val
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		
		return self.isValidSub(root,-9223372036854775808,9223372036854775807)

	def isValidSub(self,root, left, right):
		if root == None:
			return True
		else:
			if not(root.val > left and root.val <right):
				return False
			else:
				return self.isValidSub(root.left, left, root.val) and self.isValidSub(root.right, root.val, right)

        

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)
		
n1l = TreeNode(5)
# n1l.left = TreeNode(3)
# n1l.right = TreeNode(6)

n1r = TreeNode(15)
n1r.left = TreeNode(6)
n1r.right = TreeNode(20)

r = TreeNode(10)
r.left = n1l
r.right = n1r
# r = None
TN_print(r,0)
s = Solution()
n_input = r
print s.isValidBST(n_input)