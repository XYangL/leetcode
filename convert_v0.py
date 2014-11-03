# ZigZag Conversion
# !!! Time Limit Exceeded
# KP: Expected Display; Special case, nRows=1
# Exception: Input:"ABC", 2	output:"ABC"	Expected:"ACB"
# Expected Display: https://oj.leetcode.com/discuss/14105/what-does-zigzag-means
class Solution:
	# @return a string
	def convert(self, s, nRows):
		if nRows == 0:
			return ''
		elif nRows ==1:
			return s

		i = 0
		j = 0
		output = ['']*nRows
		s = list(s)
		while len(s)>0:
			for i in range(nRows):
				if (j%(nRows-1)==0) or ((i+j)%(nRows-1)==0): #!!!
					if len(s) == 0:
						break
					else:
						output[i] +=s.pop(0)
			j += 1

		return ''.join(output)

s = Solution()
n_input ='ABC'#"PAYPALISHIRING" 3
print s.convert(n_input,2)
print "PAHNAPLSIIGYIR"