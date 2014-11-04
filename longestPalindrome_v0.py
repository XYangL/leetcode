# Longest Palindromic Substring
# Wrong Answer  (3rd submit, 70 mins) [Self Design]
# KP: how to update the searh targetted substring
# KP: how to find head and update tail
# 1st Exception: 	Input:"a"	Output:""	Expected:"a"
# 2nd Exception: Input:"abadd"	Output:"dd"	Expected:"aba"	
class Solution:
	# @return a string
	def longestPalindrome(self, s):
		head = 0
		tail = len(s)-1
		sub = ''
		while head < tail :#
			# print '*',s[head:tail+1]
			for i in range(head,tail):
				if s[i] == s[tail]:
					break
			start = i
			head = i
			while s[head] == s[tail]:
				# print '\t',s[head:tail+1]
				if head == tail-1: # search all & get one 2n
					sub = s[start:head+1]
					sub +=sub[::-1]
					break
				elif head == tail-2: # search all & get one 2n*1
					sub = s[start:head+2]
					sub += sub[-2::-1]
					break
				else: # head<tail, coninue to search
					head +=1
					tail -=1
			
			#get one or h!=t
			if s[head] == s[tail]:#get one
				break
			else:#h!=t, research
				head = 0
				s = s[:-1]
				tail = len(s)-1
		if len(sub) == 0:
			sub = s[head]
		return sub
s = Solution()
n_input ="abadd"
print s.longestPalindrome(n_input)