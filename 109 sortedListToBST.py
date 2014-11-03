import math
# Convert Sorted List to Binary Search Tree 
#
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def str_val(self,level):
		re = ''
		if self != None:						
			if self.right == None:
				re += ''#\n'+str('\t'*(level+1))+'#'
			else:
				re += self.right.str_val(level+1)

			re += '\n'+str('\t'*level)+str(self.val)

			if self.left == None:
				re +=''# '\n'+str('\t'*(level+1))+'#'
			else:
				re += self.left.str_val(level+1)

		return re


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def str_val(self):
		if self.next == None:
			return '->'+str(self.val)
		else:
			return '->'+str(self.val)+ self.next.str_val()

class Solution:
	# @param head, a list node
	# @return a tree node
	def sortedListToBST(self, head):

		return self.set_suf(head,1)[1]

	def set_suf(self, list_node, index):
		if list_node.next == None: # last list node
			length = index
			formated = TreeNode(list_node.val)

		else:
			length, formated = self.set_suf(list_node.next, index+1)
			formated = self.reform(index, length, formated,TreeNode(list_node.val))

		return length, formated #l_r, parent, left, right, formated, length, sub_len

	def reform(self, index, length, root, new_node):
		mid = (length/2)+1
		# print index, length,mid, new_node.val
		# print '---- ',root.str_val(0),'\n===='
		if index > mid: # @ right
			root.right = self.reform(index-mid, length-mid, root.right, new_node)
		elif index == mid: # @ root
			new_node.right = root
			root = new_node
		else:# @ left
			root.left = self.reform(index, mid-1, root.left, new_node)
		return root 

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print head.str_val()
s = Solution()
print s.sortedListToBST(head).str_val(0)

# n2l = TreeNode(2)
# n2l.left = TreeNode(3)
# n2l.right = TreeNode(4)

# n2r = TreeNode(2)
# n2r.left = TreeNode(4)
# n2r.right = TreeNode(3)

# r = TreeNode(1)
# r.left = n2l
# r.right = n2r
# print r.str_val(0)







