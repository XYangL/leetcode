# Roman to Integer
# Accepted 704 ms
	# I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
	# 在较小的罗马数字的左边记上较大的罗马数字，表示大数字加小数字。
	# 在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字
	# 左减的数字有限制，仅限于I、X、C {}
	# [i-1] > [i] : [i]+[i-1]
	# [i-1] < [i] : [i]-[i-1] [i-1] = {I、X、C}
	# 左减时不可跨越一个位数, 左减数字必须为一位
	#: IV IX 	#: XL XC  	#: CD CM
	# 右加数字不可连续超过三位
	# 同一数码最多只能出现三次
class Solution:
	# @return an integer
	def romanToInt(self, s):
		if len(s)==0: 
			return 0
		dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		num = 0

		if len(s) == 1 : # !! onle has one char
			return dic[s]

		i = 1
		while i < len(s):
			# print i,

			small = dic[s[i-1]]<dic[s[i]]
			isThree = (s[i-1]=='I') or (s[i-1]=='X') or (s[i-1]=='C')
			if small and isThree :
				# print s[i-1],s[i],str(num),
				num -= dic[s[i-1]]
				# print '-',str(dic[s[i-1]]),'=',str(num),
				num += dic[s[i]]
				# print '+',str(dic[s[i]]),'=',str(num)
				pa = True
				i += 1
			else: # s[i-1]> = s[i]
				num += dic[s[i-1]]
				# print s[i-1], dic[s[i-1]], num

			if i == len(s)-1: # !! last char
				num += dic[s[i]]

			i += 1

		return num


s = Solution()
a = 'D' # 'MDCXCV' 1965 #'MCDXXXVII' 1437 #'XCIX' 99 #'MMXIV' 2014 #'XIV' 14
print s.romanToInt(a)

'''
Input:	"D"
Output:	0
Expected:	500

Input:	"DCXXI"
Output:	null
Expected:	621

Input:	"MDCXCV"
Output:	1690
Expected:	1695

Input:	"DCXXI"
Output:	620
Expected:	621
'''