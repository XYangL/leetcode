# Reverse Linked List II
# Accepted 120 ms 44 (1st submit, 35 mins)
# KP: Do it in-place and in one-pass.
# Kp: when m==n, return head after start
# KP: when m==1, return pre.next before end 
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		# if m==n : return head
		if m!=n:
			pre = ListNode(0)
			pre.next = head
			i = 1
			m_node = pre.next

			while m_node.next!=None and i<m:
				pre = m_node
				m_node = pre.next
				i +=1

			n_node = m_node
			post = n_node.next

			while n_node.next!=None and i<n:
				temp = post.next
				post.next = n_node
				n_node = post
				post = temp
				i +=1

			pre.next = n_node
			m_node.next = post
				
			if m ==1: #!!!
				head = pre.next
		
		return head

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
re =  s.reverseBetween(n_input,1,5)
LN_print(re)