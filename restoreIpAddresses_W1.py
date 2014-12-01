# Restore IP Addresses
# Wrong Answer
# KP: '0','0x','0xx','00x'
# Input:	"010010"
# Output:	["0.1.0.10","0.1.0.10","0.10.0.10","1.0.0.10","0.1.1.0","0.10.1.0","1.0.1.0","0.100.1.0","1.0.1.0","10.0.1.0"]
# Expected:	["0.10.0.10","0.100.1.0"]
class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		return self.checkSub(s,4)

	def checkSub(self,s,i):
		re = None
		n = len(s)
		# if n>i*3 or n<i:
		# 	re = None
		if n >=i and n<=i*3:
			if i==1:
				cut = int(s)
				if cut<256:
					re = [str(cut)+'.']
			else:
				for lastlen in range(-3,0):
					cut = s[lastlen:]
					cut = int(cut)
					if cut>255:
						continue
					else:
						temp = self.checkSub(s[:lastlen],i-1)
						if temp == None:
							continue
						else:
							if re == None:
								re = []
							for pre in temp:
								phase = pre+str(cut)
								if i!=4:
									phase +='.'
								re.append(phase)
					# print cut	
		return re

s = Solution()
n_input ="11112"
print s.restoreIpAddresses(n_input)