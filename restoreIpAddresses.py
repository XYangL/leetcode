# Restore IP Addresses
# Accepted 216 ms 147 (3rd submit, 60 mins)
# KP: backtracking

# cut = '00','01','001','010' is NOT available phase
# str(int(cut))==cut # delete the prefix '0'

# s = '', then re=[], not None
class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		return self.checkSub(s,4)

	def checkSub(self,s,i):
		re = []
		n = len(s)
		if n >=i and n<=i*3: # check length
			if i==1 and str(int(s))==s:# check '0' prefix
				cut = int(s)
				if cut<256:#check  <=255
					re = [str(cut)+'.']
			else:
				for lastlen in range(-3,0):
					cut = s[lastlen:]

					#check '0' prefix and <=255
					if (lastlen!=-1 and str(int(cut))!=cut )or int(cut)>255:
						continue
					cut = int(cut)

					#generate prefix cut
					temp = self.checkSub(s[:lastlen],i-1)
					if len(temp)==0:
						continue
					else:
						for pre in temp:
							phase = pre+str(cut)
							if i!=4:
								phase +='.'
							re.append(phase)
		return re

s = Solution()
n_input ="010010"
print s.restoreIpAddresses(n_input)