# Swap Nodes in Pairs
# Accepted 200 ms (1st submit)
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


#Given 1->2->3->4, you should return the list as 2->1->4->3.
# head = None or head.next = None, return head
# temp = head 1
# head = head.next 2
# temp.next = swapPairs(head.next) 1->(3->4)
# head.next = temp 2->1->(3->4)
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
    	
    	if head == None or head.next == None:
    		return head
    	else:
    		temp = head
    		head = head.next
    		temp.next = self.swapPairs(head.next)
    		head.next = temp
    		
    		return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# re = s.swapPairs(head)
print head.str_val()
print s.swapPairs(head).str_val()
