# Flatten Binary Tree to Linked List
# Accepted 200 ms 225 (2nd submit, 20 mins)
# KP: each node's right child points to the next node of a pre-order traversal
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return nothing, do it in place
	def flatten(self, root):
		if root != None:
			if root.left!=None or root.right!=None:# if both == None return root
				stack = [root]
				cur = TreeNode(0)
				while len(stack)!= 0:
					temp = stack.pop()
					
					if temp.right != None:
						stack.append(temp.right)
					if temp.left != None:
						stack.append(temp.left)

					cur.left = None
					cur.right = temp
					cur = cur.right

		return root

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)
	else:
		print level,' : ', None
		
n1l = TreeNode(2)
# n1l.left = TreeNode(3)
# n1l.right = TreeNode(4)

n1r = TreeNode(5)
n1r.left = TreeNode(7)
n1r.right = TreeNode(6)

r = TreeNode(1)
r.left = n1l
# r.right = n1r
# r = None
s = Solution()
n_input = r
TN_print(s.flatten(n_input),0) 