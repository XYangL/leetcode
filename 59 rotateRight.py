# Rotate List
# Accepted 268 ms

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
    	if k ==0 or head ==None or head.next == None:
    		return head
    	else:
	    	# find the old tail node and the new head node
	    	i = 0 
	    	old_tail = head
	    	new_tail = head

	    	while old_tail.next != None:
	    		old_tail = old_tail.next
	    		if i == k:
	    			new_tail = new_tail.next
	    		else:
	    			i +=1
	    	if i<k:
	    		new_k = k%(i+1)
	    		if new_k == 0:
	    			return head
	    		else:
	    			for num in range(i-new_k):
	    				new_tail = new_tail.next

'''
Input:	{1,2}, 2
Output:	{2,1}
Expected:	{1,2}

Input:	{1}, 99
Output:	{}
Expected:	{1}
'''