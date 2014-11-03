# Partition List
# Accepted 232 ms
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
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		if head != None and head.next!=None:
			temp = head
			pre_x = None
			no_less = None

			if temp.val < x:
				while temp.next.val < x:
					temp = temp.next
					if temp.next == None:
						return head
				pre_x = temp
				no_less = temp.next
			else:# temp.val >=x
				while temp.next.val >= x:
					temp = temp.next
					if temp.next == None:
						return head
				no_less = temp
				pre_x = temp.next
				no_less.next = temp.next.next
				pre_x.next = head
				head = pre_x

			while no_less.next != None:
				if no_less.next.val >= x:
					no_less = no_less.next
				else:
					temp = no_less.next
					no_less.next = temp.next
					temp.next = pre_x.next
					pre_x.next = temp
					pre_x = temp

		# print no_less.val, pre_x.val,' : ',Dummy.str_val()

		return head

head = ListNode(3)
head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)
n = 3
s = Solution()
print head.str_val()
re = s.partition(head, n)
print re.str_val()
        