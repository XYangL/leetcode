# 3Sum
# Accepted 1376 ms
class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		len_num = len(num)
		qq = 0
		oo = 0
		pp = 0
		if len_num <3 : 
			return []
		else:
			num.sort()
			result =[]

			last_i_in = len_num-2
			for i in range(len_num-2):
				if num[i] > 0 : 
					break
				last_j_in = len_num-1
				last_k_in = len_num
				for j in range(i+1, len_num-1):
					# last_j = last_i
					if j >i+1 and (num[j] == num[j-1]):
						print num[i], num[j]
						continue
					if j == last_k_in:
						break
					pp+=1
					if num[i]+num[j] >-num[j+1] : #num[i]+num[j]+num[j+1]>0
						break
					try:
						k = j+1+num[j+1:last_k_in].index(-(num[i]+num[j]))
						# print last_k_in, k
						last_k_in = k

						try:
							temp = [num[i],num[j],num[k]] 
							# i < j < k , so no need to sort temp

							result.index(temp)
							# print str(oo),temp
							oo +=1
						except Exception, e:
							result.append(temp)
							# print str(qq),temp
							qq +=1
					except Exception, e:
						pass
			
			print 'pp', str(pp)
			print 'oo', str(oo)
			print 'qq', str(qq)
			return result
	


S = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
S = [-1,0,1,2,-1,-4]
target = 0

so = Solution()

aa = so.threeSum(S)

print '\n'.join([str(i) for i in aa])
print len(aa)

'''
Input:	[-1,0,1,2,-1,-4]
Output:	[[-1,0,1]]
Expected:	[[-1,-1,2],[-1,0,1]]

Status: Time Limit Exceeded
Last executed input:	[7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]

Runtime Error
'''