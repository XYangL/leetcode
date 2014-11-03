
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
	def str_val(self):
		if self.next == None:
			return '->'+str(self.val)
		else:
			return '->'+str(self.val)+ self.next.str_val()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)