# Valid Parentheses
# Accepted 216 ms (20 mins)
# KP: Stack; 3 cases (stack&input =0, stack=0&input>0, stack>0&input=0) 
class Solution:
	# @return a boolean
	def isValid(self, s):
		dic={')':'(',']':'[','}':'{'}
		stack = []
		for ch in s:
			if ch in ['(','[','{']:
				stack.append(ch)
			else:
				if len(stack) == 0:#!!!stack=0&input>0
					return False
				left = stack.pop()
				if dic[ch] != left:
					return False
		
		if len(stack) !=0:#!!!stack>0&input=0
			return False
		
		#stack&input =0,
		return True

s = Solution()
n_input ='[]()'#"()[]{}"
print s.isValid(n_input)