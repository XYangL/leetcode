# Add Binary
# Accepted 140 ms (1st submit, 10 mins)
# KP: numeral system bin, hex, oct, int(str,num)
class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		a = int(a,2)
		b = int(b,2)

		return str(bin(a+b))[2:]

s = Solution()
n_input ='11'
b = '1'
print s.addBinary(n_input,b)