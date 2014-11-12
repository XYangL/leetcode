# Reorder List 
# Accepted 888 ms (3rd submit, 70 mins)
# KP: must do this in-place without altering the nodes' values.
# Use run/walk to split, then reverse the part after mid, 
# Finally, merge the reversed with the part before mid
# !!! remember to set mid.next == None
# !!! Read the question carefully
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if head == None or head.next == None:
			return head
		else:
			mid = head
			end = head.next
			while end.next != None:
				mid = mid.next
				end = end.next
				if end.next!= None:
					end = end.next

			post = mid.next
			mid.next = None
			post = self.reverseList(post)

			pre = head
			while pre!= None and post!= None:
				a = pre.next
				b = post.next
				post.next = a
				pre.next = post
				pre = a
				post = b
		
		return head, post				

	def reverseList(self,head):
		if head == None or head.next == None:
			return head
		else:
			a = head.next
			head.next = None
			post = a.next
			# print pre.val, a.val, post
			while post != None:
				a.next = head
				head = a
				a = post
				post = a.next
			
			a.next = head
			head = a
			return head


	def _splitList(self,head):
		fast = head
		slow = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next
			fast = fast.next

		middle = slow.next
		slow.next = None

		return head, middle


def LN_print(head):
	while head.next!=None:
		print head.val,
		head = head.next
	print head.val
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
LN_print(l1)
s = Solution()
n_input = l1
# re =  s.reorderList(n_input)
# if re!= None:
# 	LN_print(re)
# else:
# 	print None


a,b = s.reorderList(l1)
LN_print(a)
# LN_print(b)



