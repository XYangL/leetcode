# Length of Last Word
# Accepted 168 ms (1st Submit, 20 mins)
class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLastWord(self, s):
		len_last = 0
		length = len(s)
		
		if length != 0:
			get_ch = False
			for i in range(length):
				if s[length-1-i] !=' ':
					if not get_ch:
						get_ch = True
					len_last +=1
				else:# s[length-i] == ' '
					if get_ch:
						break
					else:
						continue


		return len_last


s = Solution()
st = 'this'#'hello world'
print s.lengthOfLastWord(st)
