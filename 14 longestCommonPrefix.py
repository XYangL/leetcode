# Longest Common Prefix
# Accepted 156 ms (1st submit)
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	# len = 0 return ''
    	# len = 1 return strs[0]
    	length = len(strs)
    	com = ''
    	if length == 1:
    		return strs[0]
    	elif length >1:
    		com = strs[0]
    		for one in strs[1:]:
    			com_len = min([len(com),len(one)])
    			while (com_len != 0) and (com[:com_len] != one[:com_len]):
    					com_len -= 1
    			if com_len == 0:
	    			return ''
	    		else:
	    			com = com[:com_len]
    	return com


s = Solution()
strs = ['aa','ab','c']#['this','the','th']
print s.longestCommonPrefix(strs)
        