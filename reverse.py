# Reverse Integer 
# Accepted  296 ms (1st submit, 20mins)
# KP: 0, zero; reverse, end with 0; integer overflow
class Solution:
	# @return an integer
	def reverse(self, x):
		mul = 1
		if x < 0 :
			mul = -1
		x *= mul
		x = str(x)[::-1]

		output =  mul*int(x)
		return output
        

s = Solution()
n_input = -1000
print s.reverse(n_input)



