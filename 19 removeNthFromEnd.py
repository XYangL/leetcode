# Remove Nth Node From End of List 
# Accepted 204 ms
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
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(0)
		dummy.next = head

		tail = dummy
		for i in range(n):
			tail = tail.next

		prefix = dummy
		while tail.next != None:
			tail = tail.next
			prefix = prefix.next

		prefix.next = prefix.next.next

		return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s=Solution()
re = s.removeNthFromEnd(head, 2)
print re.str_val()
        