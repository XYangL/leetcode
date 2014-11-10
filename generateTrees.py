# Unique Binary Search Trees II 
# Accepted 312 ms 9 (1st submit, 60 mins)
# KP: DP;  n=0 => [{}]
# KP: After appending root to result, 
#     root has to be reconstructed or renewed by set children to None 
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @return a list of tree node
	def generateTrees(self, n):
		if n == 0:
			return [None]#!!!
		
		nodes = range(1,n+1)#[TreeNode(i) for i in range(1,n+1)]
		return self.generateSub(nodes,n)
		
	def generateSub(self, nodes, n):
		# print n,nodes
		if n == 0:
			return [None]
		if n == 1:# n= 0/1
			return [TreeNode(nodes[0])]

		result = []

		for i in range(0,n):
			# root = TreeNode(nodes[i])
			for left in self.generateSub(nodes[:i],i):
				for right in self.generateSub(nodes[i+1:],n-i-1):
					root = TreeNode(nodes[i]) #!!!
					root.left = left
					root.right = right
					result.append(root)
		# 			if n == 3:
		# 				print '-'*10,nodes[i],'-'*10
		# 				TN_print(root,0)
		return result

def TN_print(node,level):# level[root]=0
	if node!= None:
		print level,' : ', node.val
		TN_print(node.left,level+1)
		TN_print(node.right,level+1)
	else:
		print level,' : #'
	
s = Solution()
n_input = 3
re=s.generateTrees(n_input)
print 'Num =',len(re)
for i in re:
	print '-'*10,i.val,'-'*10
	TN_print(i,0)
