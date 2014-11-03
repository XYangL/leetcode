# Merge Sorted Array 
# !! a linear solution is to fill the arrays from the end back to the start
class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		if m!= 0 and n!=0:
			# A points to Small
			all_in = m
			if A[0]>B[0]:
				temp = A
				A = B
				B = temp

				temp = m
				m = n
				n = temp
			
			# A[0]<= B[0]
			i = 1
			j = 0
			# print A[i], B[j]
			while i < m and j < n:
				if A[i]<= B[j]:
					i +=1
				else:
					A = A[0:i]+[B[j]]+A[i:m]
					j +=1
					m +=1

			if j <n :
				A = A[0:m] + B[j:n]
		else:			
			A = A[0:m]+B[0:n]

		print A




        

# A = [1,3,5,7,9]
# B = [0,4,6,8,10]

A = []
B = [1]

print A
print B

s = Solution()       
s.merge(A,len(A),B,len(B))

# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space 
# (size that is greater or equal to m + n) 
# to hold additional elements from B. 

# The number of elements initialized in A and B are m and n respectively.