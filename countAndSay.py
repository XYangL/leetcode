# Count and Say 
# Accepted 144 ms (1st submit, 30mins)

class Solution:
	# @return a string
	def countAndSay(self, n):
		output = '1'
		ith = 1
		while ith<n:
			temp =''
			name = output[0]
			num = 1
			for i in range(1,len(output)) :
				if output[i] == name:
					num += 1
				else:
					temp += str(num) +name
					name = output[i]
					num = 1

			output = temp + str(num) + name
			ith += 1

		return output

s = Solution()
n_input = 6
print s.countAndSay(n_input)



