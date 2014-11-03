# Merge Two Sorted Lists 
# Accepted 288 ms
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
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		elif l2 == None:
			return l1

		if l1.val > l2.val:
			temp = l2
			l2 = l1
			l1 = temp
		head = l1 # l1 point to small head

		while l2 != None:
			if l1.next == None:
				l1.next =l2
				break
			else:
				while l1.next.val <= l2.val:
					l1 = l1.next
					if l1.next == None:
						break
				# l1.next.val > l2
				temp = l2
				l2 = l2.next
				temp.next = l1.next
				l1.next = temp
				l1 = l1.next
		return head

l1 = ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(7)


l2 = ListNode(1)
l2.next = ListNode(4)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(8)

print 'l1',l1.str_val()
print 'l2',l2.str_val()

s= Solution()
re = s.mergeTwoLists(l1, l2)
print 're',re.str_val()
