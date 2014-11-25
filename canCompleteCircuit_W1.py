# Gas Station
# Time Limit Exceeded
# KP: 
class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		left = -1
		start = []
		
		for i in range(len(gas)):
			temp = gas[i]-cost[i]
			if temp > left:
				left = temp
				start = [i]
			elif left>0 and temp == left:
				start.append(i)

		if len(start) == 0:
			return -1

		for s in start:
			# print s
			gas_rotated = gas[s:]+gas[:s]
			cost_rotated = cost[s:]+cost[:s]

			tank = 0
			for i in range(len(gas)):
				tank = tank+gas_rotated[i]-cost_rotated[i]
				# print i, tank, gas_rotated[i],cost_rotated[i],temp
				if tank < 0:
					break
			
			if tank >=0:
				start = s
				break

		if tank <0:
			return -1

		return start

s = Solution()
# gas = [1,2,3,4,5]#[2,3,1]#[2,3,4,8,5,6,7]
# cost= [3,4,5,1,2]#[3,1,2]#[5,2,4,9,5,5,5]
gas = [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
cost = [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
print s.canCompleteCircuit(gas, cost)