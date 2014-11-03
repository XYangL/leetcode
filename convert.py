# ZigZag Conversion
# Accepted 444 ms ( 60 mins)
class Solution:
	# @return a string
	def convert(self, s, nRows):
		if nRows == 1:
			return s
		output = ['']*nRows
		s = list(s)
		for i in range(len(s)):
			temp = i%(2*nRows-2)
			if temp < nRows:
				output[temp] +=s[i]
			else:
				output[2*nRows-2-temp]+=s[i]

		return ''.join(output)

s = Solution()
n_input ="PAYPALISHIRING"
print s.convert(n_input,3)
print "PAHNAPLSIIGYIR"