# Binary Tree Level Order Traversal
# Accepted 264 ms (1st Submit)
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
		num = []
		if root == None or root.val =='#':
			return num
		else:
			return self.get_k(1,num, root)

	def get_k(self, k, num, node):
		if len(num) < k:
			num.append([])
		num[k-1] += [node.val]

		if node.left != None:
			if node.left.val != '#':
				num = self.get_k(k+1, num, node.left)
		if node.right != None:
			if node.right.val != '#':
				num = self.get_k(k+1, num, node.right)
		return num



s = Solution()

n9 = TreeNode(9)
n9.left = TreeNode(4)
n9.right = TreeNode('#')

n20 = TreeNode(20)
n20.left = TreeNode(5)
n20.right = TreeNode('#')

r = TreeNode(3)
r.left = n9
r.right = n20
# '\n'.join([i for i in s.levelOrder(r)])
print s.levelOrder(r)