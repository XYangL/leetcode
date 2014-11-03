# Maximum Depth of Binary Tree
# Accepted 332 ms
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            dep = max[left,right] + 1
            return dep
                
'''
Runtime Error Message:  Line 15: NameError: global name 'left' is not defined
Last executed input:    {0}
'''        