# Validate Binary Search Tree
# Wrong Answer
# Input: {10,5,15,#,#,6,20}		Output: True	Expected: false
# KP: left_max/most right < node.val < right_min/mostleft
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
		if root == None:
			return True
		else:
			isValidLeftSub = False
			isValidLeftChild = False
			isValidRightSub = False
			isValidRightChild = False

			if root.left!= None:
				isValidLeftSub = self.isValidBST(root.left)
				if not isValidLeftSub:
					return False
				isValidLeftChild = (root.left.val<root.val)
				# print isValidLeftChild,root.left.val,root.val,'=>',
			else:
				isValidLeftSub = True
				isValidLeftChild = True

			if root.right!= None:
				isValidRightSub = self.isValidBST(root.right)
				if not isValidRightSub:
					return False
				isValidRightChild = (root.right.val>root.val)
			else:
				isValidRightSub = True
				isValidRightChild = True
			re = isValidLeftSub and isValidLeftChild and isValidRightSub and isValidRightChild
			# print root.val, re ,':', isValidLeftSub , isValidLeftChild , isValidRightSub , isValidRightChild
		return re
        
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