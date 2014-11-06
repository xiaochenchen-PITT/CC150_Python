# s = '1101'
# l = []
# for i in xrange(0, len(s)):
# 	pre = s[:i]
# 	this = str(1 - int(s[i]))
# 	post = s[i+1:]
# 	l.append(pre+this+post)
# print l

class Solution:
    # @return a list of integers
    def grayCode(self, n):
    	# DFS
    	# Exponential time complexity
        s = '0'*n
        self.res = [s]
        self.DFS(s, n)
        return self.res

    def DFS(self, s, n):
    	if len(self.res) == 2**n:
    		return
    	next_grays = []
        for i in xrange(0, len(s)):
        	pre = s[:i]
        	this = str(1 - int(s[i]))
        	post = s[i+1:]
        	next_grays.append(pre+this+post)
        # print 's, next_grays : ', s, next_grays
        for next in next_grays:
        	if next not in self.res:
        		self.res.append(next)
        		self.DFS(next, n)

    def grayCode2(self, n):
    	# Bit manipulation
    	# Gray = (Bin >> 1) ^ Bin
    	res = []
    	for n in xrange(0, 2**n):
    		res.append((n>>1) ^ n)
    	return res

s = Solution()
print s.grayCode(4)
print s.grayCode2(4)
