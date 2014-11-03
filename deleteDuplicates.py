# Remove Duplicates from Sorted List
# Accepted 300 ms (1st submit, 15 mins)
# KP: 
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
	    self.val = x
	    self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head == None or head.next == None:
			return head
		else:
			cur = head
			while cur.next != None:
				pre = cur
				cur = cur.next
				if pre.val == cur.val:
					pre.next = cur.next
					cur = pre
		return	head

head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
s = Solution()
n_input = head
re = s.deleteDuplicates(n_input)

while re.next!= None:
	print re.val
	re = re.next
print re.val