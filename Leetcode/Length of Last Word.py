class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
    	return len(s.strip().split(' ')[-1])
    	# same as...
    	s = s.strip(' ') # str.strip() return a new str
    	print s
    	l = s.split(' ') # str.split() return a list
    	print l
        return len(l[-1])

s = Solution()
print s.lengthOfLastWord(' this is ')