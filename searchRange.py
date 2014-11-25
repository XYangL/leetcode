# Search for a Range
# Accepted 304 ms 81 (1st submit, 35 mins)
# KP: Binary search
class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		head = -1
		end = -1
		n =len(A)
		mid = n/2
		if A[mid]<target:
			head = self.gethead(A,target,mid+1,n-1)
			end = self.getend(A,target,mid+1,n-1)
		elif A[mid]== target:
			head = self.gethead(A,target,0,mid-1)
			if head == -1:
				head = mid
			end = self.getend(A,target,mid+1,n-1)
			if end == -1:
				end = mid

		else:#A[mid]>target:
			head = self.gethead(A,target,0,mid-1)
			end = self.getend(A,target,0,mid-1)

		return [head,end]

	def gethead(self,A,target,a,b):
		if a>b:
			return -1
		elif a==b :
			if A[a]== target:
				return a
			else:
				return -1
		else:
			mid = (a+b)/2
			if A[mid]<target:
				head = self.gethead(A,target,mid+1,b)
			elif A[mid]== target:
				head = self.gethead(A,target,a,mid-1)
				if head ==-1:
					head = mid
			else:#A[mid]>target:
				head = self.gethead(A,target,a,mid-1)
			return head

	def getend(self,A,target,a,b):

		if a>b:
			return -1
		elif a==b :
			if A[a]== target:
				return a
			else:
				return -1
		else:

			mid = (a+b)/2
			if A[mid]<target:
				end = self.getend(A,target,mid+1,b)
			elif A[mid]== target:
				end = self.getend(A,target,mid+1,b)
				if end == -1:
					end = mid
			else:#A[mid]>target:
				end = self.getend(A,target,a,mid-1)
			return end

s = Solution()
n_input =[5, 7, 7, 8, 8, 10]
print s.searchRange(n_input,8)