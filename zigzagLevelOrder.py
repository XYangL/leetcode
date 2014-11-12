# Binary Tree Zigzag Level Order Traversal
# Accepted 184 ms (2nd submit, 25 mins)
# KP: Queue ; Return [] when root = None
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def TN_print(node,level):# level[root]=0
		if node!= None:
			print level,' : ', node.val
			TN_print(node.left,level+1)
			TN_print(node.right,level+1)

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		if root == None:
			return [] # not return None
		else:
			Que = []
			Que.append((root,0))
			level = []
			while len(Que) > 0:
				(node,n) = Que[0]
				Que = Que[1:]

				if n == len(level):
					level.append([node.val])
				else:
					level[n].append(node.val)

				if node.left != None:
					Que.append((node.left, n+1))
				if node.right != None:
					Que.append((node.right,n+1))

			# print level

			for i in range(1,len(level),2):
				level[i]= level[i][::-1]

		return level

s = Solution()
		
n1l = TreeNode(2)
# n1l.left = TreeNode(4)
# n1l.right = TreeNode(5)

n1r = TreeNode(20)
n1r.left = TreeNode(15)
n1r.right = TreeNode(7)

r = TreeNode(1)
r.left = n1l
# r.right = n1r
#r = None
n_input = r
print s.zigzagLevelOrder(n_input)