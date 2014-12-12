# Spiral Matrix
# Accepted 108 ms 21 (2nd submit, 150  mins)
# KP: 
class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		m = len(matrix)
		if m==0:
			return []
		else:
			n = len(matrix[0])
			steps = [[0,1,n],[1,0,m-1],[0,-1,n-1],[-1,0,m-2]]
			re = []
			len_re = m*n
			i = 0
			j = -1

			a = 0
			while len(re)<len_re:
				for s in steps:
					for times in range(s[2]):
						i +=s[0]
						j +=s[1]
						re.append(matrix[i][j])

					s[2] -= 2
					if len(re)==len_re:
						break
				# print 'here'
				# i +=1
				# j +=1

				# a+=1
				# if a>10: exit()

			return re

s = Solution()
n_input = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]]
#[[1,2],[4,3]]#[[ 1, 2, 3 ,4],[ 12, 13, 14,5 ],[ 11, 16,15, 6 ],[10,9,8,7]]
#[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print s.spiralOrder(n_input)