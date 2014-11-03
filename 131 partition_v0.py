# Palindrome Partitioning
# Accepted 1296 ms

global t
t = ''
def ppartition(s):
	global t
	print t+'s='+s
	result = []
	if len(s) ==1:
		return [[s]]
	for sub_1_len in range(1,len(s)):
		print sub_1_len,range(1,len(s))
		sub_1 = s[0:sub_1_len]
		is_palindrome = True

		for i in range(sub_1_len/2):
			if sub_1[i] != sub_1[sub_1_len-1-i]:
				is_palindrome = False
				i = sub_1_len
		
		if is_palindrome:
			print t+sub_1+'='+str(is_palindrome)+'\t' +s[sub_1_len:]
			t +='\t'
			left_palindrome= partition(s[sub_1_len:])
			t = t[0:-1]
			if left_palindrome == []:
				return []
			else:
				result +=[[sub_1]+left_sub for left_sub in left_palindrome]	
	
	sub_1 = s
	is_palindrome = True
	for i in range(len(s)/2):
		if sub_1[i] != sub_1[len(s)-1-i]:
			is_palindrome = False
			i = sub_1_len
	if is_palindrome: 
		result +=[[s]]

	# print t+str(result)
	return result		

def partition(s):
	result = []
	if len(s) ==1:
		return [[s]]
	for sub_1_len in range(1,len(s)):
		sub_1 = s[0:sub_1_len]
		is_palindrome = True

		for i in range(sub_1_len/2):
			if sub_1[i] != sub_1[sub_1_len-1-i]:
				is_palindrome = False
				i = sub_1_len
		
		if is_palindrome:
			left_palindrome= partition(s[sub_1_len:])
			if left_palindrome == []:
				return []
			else:
				result +=[[sub_1]+left_sub for left_sub in left_palindrome]
	
	sub_1 = s
	is_palindrome = True
	for i in range(len(s)/2):
		if sub_1[i] != sub_1[len(s)-1-i]:
			is_palindrome = False
			i = sub_1_len
	if is_palindrome: 
		result +=[[s]]

	return result	


s = "bb"
o = partition(s)
print o