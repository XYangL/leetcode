# Generate Parentheses
# Accepted 116 ms 8 
# KP: https://oj.leetcode.com/discuss/11509/an-iterative-method
# f(0) =''
# f(3) = ( f(0) ) f(2), ( f(1) ) f(1),( f(2) ) f(0)
# f(n) = ( f(0) ) f(n-1-0), ( f(1) ) f(n-1-1), ..., ( f(i) ) f(n-1-i), ..., ( f(n-1) ) f(0)

class Solution:
	# @param an integer
	# @return a list of string
	def generateParenthesis(self, n):
		dic = {}
		if n >= 0:
			dic = {0:['']}
		if n >=1:
			num = 1
			while num <=n:
				temp = []
				for i in range(num):# 0<=i<=num-1
					j = num -1 - i # i+j = num-1
					for pre in dic[i]:
						for post in dic[j]:
							one = '('+pre+')'+post
							temp.append(one)
				dic[num]= temp
				num +=1

		return dic[n]

s = Solution()
n_input = 4
# print s.generateParenthesis(n_input)
re = s.generateParenthesis(n_input)
correct = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
for i in re:
	correct.remove(i)
if len(correct)==0:
	print 'Yes'