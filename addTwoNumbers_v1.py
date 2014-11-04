# Add Two Numbers
# Accepted 656 ms (1st submit, 50 mins)
# KP:  Boundary Condition
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		if l1 == None:
			return l2
		elif l2 == None:
			return l1
		else:
			head = l1
			tag = 0
			while l1.next!=None and l2.next!=None:
				l1.val += l2.val+tag
				if l1.val >= 10:
					l1.val -= 10
					tag = 1
				else:
					tag = 0
				l1 = l1.next
				l2 = l2.next

			if l1.next == None:
				l1.next = l2.next
				l2.next = None

			if l1.next == None:# Both .next are None
				l1.val += l2.val+tag
				if l1.val >= 10:
					l1.val -= 10
					l1.next = ListNode(1)
			else:#l1.next != None, l2.next==None
				tail = l1
				tag = l2.val+tag #!!!
				while tag: # tag>0
					tail.val += tag
					if tail.val >= 10:
						tail.val -=10
						if tail.next == None:#!!!
							tail.next = ListNode(1)
							break
						else:
							tag = 1
							tail = tail.next
					else :
						tag = 0
			return head

def LN_print(head):
	while head.next!=None:
		print head.val,
		head = head.next
	print head.val

s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(8)
# l1.next.next.next = ListNode(9)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)
LN_print(l1)
LN_print(l2)
l = s.addTwoNumbers(l1,l2)
LN_print(l)