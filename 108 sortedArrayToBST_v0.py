# Convert Sorted Array to Binary Search Tree
# Not a Binary Search Tree
# BST should l <= c <= r
# but this return c < l < r
# Definition for a  binary tree node
t = ''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def print_val(self):
		global t
		print t , self.val
		t = t+'\t'
		if  self.left != None:	
			self.left.print_val()
		else: 
			print t ,'#'
		if self.right != None:
			self.right.print_val()
		else:
			print t ,'#'
		t = t[0:-1]

class Solution:
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):
		TN = None
		length = len(num)
		if length >= 1:
			TN = self.setNode(1, num, length)
		return TN

	def setNode(self, index, num, l):
		TN = None
		if index <= l :
			# print index, l , num, num[0]
			TN = TreeNode(num[index-1])
			TN.left = self.setNode(index*2, num, l)
			TN.right = self.setNode(index*2+1, num, l)
		return TN

s = Solution()
num = [1,2,3,4,5,6]
re = s.sortedArrayToBST(num)
if re != None:
	re.print_val()
print re

