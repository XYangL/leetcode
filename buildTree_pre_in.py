# Construct Binary Tree from Preorder and Inorder Traversal
# Accepted 1080 ms 202 (1st submit, 20  mins)
# KP: 1st of Preorder is the root
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		root = None
		if len(preorder) !=0:
			root = TreeNode(preorder[0])
			i = inorder.index(root.val)
			root.left = self.buildTree(preorder[1:i+1], inorder[:i])
			root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
		return root

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)

pre = 'A B D C E G H F I'.split()
ino = 'D B A G E H C F I'.split()
s = Solution()
re = s.buildTree(pre,ino)
TN_print(re,0)