# Spiral Matrix II 
# Accepted 100 ms 21 (2nd submit, 35 mins)
# KP: n is integer which is possible <= 0
class Solution:
	# @return a list of lists of integer
	def generateMatrix(self, n):

		if n ==0:
			return []
		elif n<0:
			n = -n
		mat = []
		for i in range(n):
			mat.append([0]*n)
		return self.fillSub(mat,1,n,0)

	def fillSub(self,mat,start,step,i):
		if step == 1:
			mat[i][i]=start
		elif step ==2:
			mat[i][i]=start
			mat[i][i+1]=start+1
			mat[i+1][i+1]=start+2
			mat[i+1][i]=start+3
		else:
			mat = self.fillSub(mat,start+4*step-4,step-2,i+1)
			moves = [(0,1),(1,0),(0,-1),(-1,0)] #!!!
			j=i
			for move in moves:
				for times in range(step-1): # number of steps per edge
					mat[i][j] = start

					i +=move[0]
					j +=move[1]
					start +=1

		return mat

s = Solution()
n_input =6
# print s.generateMatrix(n_input)
for i in s.generateMatrix(n_input):
	print i