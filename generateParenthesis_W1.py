# Generate Parentheses
# Wrong Answer
# KP: n ==4, cannot generate :'(())(())'
class Solution:
	# @param an integer
	# @return a list of string
	def generateParenthesis(self, n):
		if n == 0:
			re = []
		if n == 1:
			re = ['()']
		else:
			re = []
			temp = self.generateParenthesis(n-1)
			for i in temp:
				re.append('('+i+')')
			for i in temp:
				re.append('()'+i)

			for i in temp:
				if i[0:2]!='()':
					re.append(i+'()')

		return re

s = Solution()
n_input = 4
# print s.generateParenthesis(n_input)
re = s.generateParenthesis(n_input)
correct = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
print len(re),len(correct)
for i in re:
	correct.remove(i)
print correct