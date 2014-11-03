# Gray Code 
# Accepted 240 ms 
# !! return is integers
# realte binary processing to integer
class Solution:
	# @return a list of integers
	def grayCode(self, n):
		CB = [0] # codes book
		if n>0:
			for i in range(n):
				new_CB = []
				for code in CB[::-1]:
					new_CB = [code]+new_CB+[2**i+code] # !!
				CB = new_CB
			# print str(n)+'_CB= ', CB
		
		return CB



s = Solution()
n = 2

print '\n'.join([str(i) for i in s.grayCode(n)])


'''
Binary Formart
	def grayCode(self, n):
		CB = [''] # codes book
		if n>0:
			new_CB = []
			for i in range(n):
				new_CB = []
				for code in CB[::-1]:
					new_CB = ['0'+code]+new_CB+['1'+code]
				CB = new_CB
			# print str(n)+'_CB= ', CB
		
		CB = [int(i,2) for i in CB]
		return CB
'''
        