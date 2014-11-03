# Container With Most Water 
# Accepted 428 ms
class Solution:
	# @return an integer
	def maxArea(self, height):
		if len(height) < 2:
			return 0
		else:
			l = 0
			r = len(height)-1
			area = (r-l)*min([height[l],height[r]])
			while(l<r):
				if height[l] > height[r] :
					r -=1
				else:
					l +=1
				new_area = (r-l)*min([height[l],height[r]])
				area = max([area, new_area])
			
			return area




h = [1,2,1,1,6]
s = Solution()
print s.maxArea(h)

    