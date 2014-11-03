# 3Sum
# Runtime Error
class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		result = []
		if len(num)>=3:
			num.sort()
			dic = {}

			for nc in range(2,len(num)):
				# update dic
				for i in range(nc-1):
					for j in range(i+1,nc):
						key = num[i]+num[j]
						if dic.has_key(key):
							dic[key] = self.merge(dic[key],(num[i],num[j]))
						else:
							dic[key] = [(num[i],num[j])]
				# find the tuples

				key = -num[nc] 
				if dic.has_key(key):
					for pair in dic[key]:
						temp = [num[nc], pair[0],pair[1]]
						temp.sort()
						try:
							result.index(temp)
						except Exception, e:
							result.append(temp)
		return result
	
	#@param vals, a list of tuples, every tuple has two integer, e.g. [(2,1),...,(4,2)]
	#@param new_val, a new tuple (a,b), where b >=a
	#@return new_val, a list of tuples
	def merge(self, vals, new_val):
		try:
		 	vals.index(new_val)
		except :
		 	vals.append(new_val)
		return vals
	


S = [0,0,0]
target = 0

so = Solution()

aa = so.threeSum(S)

print '\n'.join([str(i) for i in aa])
print len(aa)
