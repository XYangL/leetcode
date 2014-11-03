# Palindrome Partitioning
# Accepted 1296 ms
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
		result = []
		if len(s) ==1:
			return [[s]]
		for sub_1_len in range(1,len(s)):
			sub_1 = s[0:sub_1_len]
			is_palindrome = True

			for i in range(sub_1_len/2):
				if sub_1[i] != sub_1[sub_1_len-1-i]:
					is_palindrome = False
					i = sub_1_len
			
			if is_palindrome:
				left_palindrome= self.partition(s[sub_1_len:])
				if left_palindrome == []:
					return []
				else:
					result +=[[sub_1]+left_sub for left_sub in left_palindrome]
		sub_1 = s
		is_palindrome = True
		for i in range(len(s)/2):
			if sub_1[i] != sub_1[len(s)-1-i]:
				is_palindrome = False
				i = sub_1_len
		if is_palindrome: 
			result +=[[s]]
		return result

'''
Input:	"abbab"
Output:	[["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"]]
Expected:	[["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]

Input:	"cdd"
Output:	[]
Expected:	[["c","d","d"],["c","dd"]]

Input:	"ab"
Output:	[["a","b"],["ab"]]
Expected:	[["a","b"]]

Input:	"bb"
Output:	[["b","b"]]
Expected:	[["b","b"],["bb"]]
'''