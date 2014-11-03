# Convert Sorted Array to Binary Search Tree
# Accepted 388 ms
# 1. length == 0
# 2. a%2 == 0, then a/2 == (a+1)/2
# since in BST, left < center < right 
# and num is ascending, num[i]<num[i+1]:
# 	left = num[0:a/2]
# 	center = num[a]
# 	right = num [a+1:]
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
			a = length / 2
			TN = TreeNode(num[a])
			TN.left = self.sortedArrayToBST(num[0:a])
			TN.right = self.sortedArrayToBST(num[a+1:])
		return TN

s = Solution()
num = [1,3,4]
re = s.sortedArrayToBST(num)
if re != None:
	re.print_val()
print re

'''
Runtime Error

Input:	[1,3]
Output:	{1,3}
Expected:	{3,1}
'''