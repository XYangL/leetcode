# Convert Sorted List to Binary Search Tree
# Accepted [Cost nearly one day to finish]
# !!! There should be better solution using Pointer in other Language
# KP: 2 Pointer/step;
# KP: No Pointer in Python, so no all method is possible, e.g. Create Nodes Bottom-Up
# ?? https://oj.leetcode.com/discuss/14113/sorted-list-to-binary-search-tree-o-nlogn-time-complexity
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
#
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
def LN_print(head):
	while head.next!=None:
		print head.val,
		head = head.next
	print head.val

class Solution:
	# @param head, a list node
	# @return a tree node
	def sortedListToBST(self, head):
		point = head
		length = 0
		array = []
		while point!= None:
			array += [point.val]
			point = point.next

		root = self.sortedArrayToBst(array, 0, len(array)-1)

		return	root

	def sortedArrayToBst(self, array, start, end): #!!!
		if start > end:#!!!
			return None
		elif start == end:
			return TreeNode(array[start])
		else:
			mid = (start+end)/2
			root = TreeNode(array[mid])
			root.left = self.sortedArrayToBst(array,start,mid-1)
			root.right = self.sortedArrayToBst(array,mid+1,end)
			return root


s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
print 'l1: ',
LN_print(l1)
n_input =l1
re=s.sortedListToBST(n_input)

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)
TN_print(re,0)