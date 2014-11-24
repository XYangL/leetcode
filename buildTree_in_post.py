# Construct Binary Tree from Inorder and Postorder Traversal
# Accepted 1036 ms 202 (1st submit, 10 mins)
# KP: 
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		root = None
		if len(postorder)!=0:
			root = TreeNode(postorder[-1])
			i = inorder.index(root.val)
			root.left = self.buildTree(inorder[:i],postorder[:i])
			root.right = self.buildTree(inorder[i+1:],postorder[i:-1])

		return root

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)
		
ino = 'D B A G E H C F I'.split()
post = 'D B G H E I F C A'.split()
s = Solution()
re =  s.buildTree(ino,post)
TN_print(re,0)