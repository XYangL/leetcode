# Populating Next Right Pointers in Each Node 
# Accepted 264 ms (1st submit, 4 hours)
# KP: Make use of self.next 
# Idea: link from root level to leaf level; link from left to right for each level
# Idea From: https://oj.leetcode.com/discuss/10163/my-tail-recursion-answer
# https://oj.leetcode.com/discuss/7327/a-simple-accepted-solution
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

	def printN(self):
		if self.next !=None:
			print self.val,'->',self.next.val
		if self.left!=None:
			self.left.printN()
		if self.right!=None:
			self.right.printN()

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		line = root
		if line!= None:
			while line.left != None:
				a = line
				b = line.next
				a.left.next = a.right
				
				while b!=None:	
					a.right.next = b.left
					a = b
					b = a.next
					a.left.next = a.right

				line = line.left


		# connect(a.right)

		return root

n1l = TreeNode(2)
n1l.left = TreeNode(4)
n1l.right = TreeNode(5)

n1r = TreeNode(3)
n1r.left = TreeNode(6)
n1r.right = TreeNode(7)

r = TreeNode(1)
r.left = n1l
r.right = n1r

s = Solution()
n_input =r
s.connect(n_input).printN()