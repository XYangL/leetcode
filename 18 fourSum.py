# 4Sum
# Accepted 1372 ms
class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		result = []
		if len(num)>=4:
			num.sort()
			dic = {}

			for i in range(len(num)-1):
				for j in range(i+1,len(num)):
					key = target - (num[i]+ num[j])
					if dic.has_key(key):
						for pair in dic[key]:
							temp = [num[j],num[i],pair[0],pair[1]]
							temp.sort()
							try:
								result.index(temp)
							except Exception, e:
								result.append(temp)
				
				for j in range(i):
					key = num[i]+ num[j]
					if dic.has_key(key):
						dic[key] = self.merge(dic[key],(num[j],num[i]))
					else:
						dic[key] = [(num[j],num[i])]
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
	


S = [ 1,0,-1,0,-2,2 ]
target = 0

so = Solution()

aa = so.fourSum(S,target)

print '\n'.join([str(i) for i in aa])
print len(aa)

'''
Status: Time Limit Exceeded
Last executed input:	[-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497], 3032

Internal Error

Status: Time Limit Exceeded
Last executed input:	[-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488], -2808

Input:	[0,0,0,0], 0
Output:	null
Expected:	[[0,0,0,0]]


Status: Time Limit Exceeded
Last executed input:	[], 0
'''