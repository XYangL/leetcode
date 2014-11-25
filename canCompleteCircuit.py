# Gas Station
# Accepted 208 ms 13
# KP: Greedy Alg
# Idea From : http://chaoren.is-programmer.com/posts/43583.html
class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		if sum(gas)<sum(cost):
			return -1

		temp = 0
		start = 0
		
		for i in range(len(gas)):
			temp += gas[i]-cost[i]
			if temp < 0:
				start = i+1
				temp = 0

		return start

s = Solution()
gas = [1,2,3,4,5]#[2,3,1]#[2,3,4,8,5,6,7]
cost= [3,4,5,1,2]#[3,1,2]#[5,2,4,9,5,5,5]
# gas = [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
# cost = [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
print s.canCompleteCircuit(gas, cost)