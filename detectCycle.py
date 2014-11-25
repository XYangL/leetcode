# Linked List Cycle II
# Accepted 716 ms 16 (2nd submit, 35 mins)
# KP: Two Pointers
# http://chaoren.is-programmer.com/posts/43272.html
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		start = None
		if head != None:
			slow = head
			fast = head.next #!!!
			
			while fast!=None and slow!= fast:
				fast = fast.next
				if fast == None:
					break
				else:
					fast = fast.next
					slow = slow.next

			if fast != None:
				fast = head
				slow = slow.next #!!!
				while fast != slow:
					fast = fast.next
					slow = slow.next
				start = fast
		return start

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)
l2.next.next.next = l2

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = l2

s = Solution()
n_input = l1
print s.detectCycle(n_input).val