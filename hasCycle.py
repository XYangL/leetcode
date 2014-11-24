# Linked List Cycle
# Accepted 572 ms 16 (2st submit,  mins)
# KP: Two Pointer
# Definition for singly-linked list.
# Idea From: http://chaoren.is-programmer.com/posts/43022.html
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		slow = quick = head #!!!
		while quick != None and quick.next!= None:
			slow = slow.next
			quick = quick.next.next
			if slow == quick:#!!!
				return True
		return False

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = l1#ListNode(4)

s = Solution()
n_input =l1
print s.hasCycle(n_input)