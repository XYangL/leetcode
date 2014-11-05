# Merge Sorted Array 
# Accepted 180 ms
# KP:A has enough space (size that is greater or equal to m + n)
# KP:!! So a linear solution is to fill the arrays from the end back to the start
class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		i = m-1
		j = n-1
		c = m+n-1

		while i >= 0 and j >= 0:
			if A[i]<= B[j]:
				A[c] = B[j]
				j -=1
			else:
				A[c] = A[i]
				i -=1
			c -= 1

		# Time Limit Exceededb !!! Set Slice => O(k+n)
		# if i <0 :
		# 	A[:j+1]=B[:j+1]
		
		# Accepted
		while j>=0:
			A[j]=B[j]
			j-=1
		#else: #j<0 A[:i+1]= A[:i+1]			
			
		print A

B = [0,4,6,8,10]
A = [1,3,5,7]+[0]*len(B)n = len(B)
m = len(A)-n
# A = []
# B = []
print 'A',A
print 'B',B

s = Solution()       
s.merge(A,m,B,n)

# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space 
# (size that is greater or equal to m + n) 
# to hold additional elements from B. 

# The number of elements initialized in A and B are m and n respectively.