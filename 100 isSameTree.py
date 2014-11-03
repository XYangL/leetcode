# Same Tree
# Accepted 172 ms
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif (p!= None and q== None) or (p== None and q!= None):
            return False
        elif p.val != q.val:
            return False
        else:
            equalleft = isSamTree(p.left, q.left)
            equalright = isSameTree(p.right, q.right)
            return equalleft and equalright
            
'''
Runtime Error Message:  Line 20: NameError: global name 'isSamTree' is not defined
Last executed input:    {0}, {0}
'''        