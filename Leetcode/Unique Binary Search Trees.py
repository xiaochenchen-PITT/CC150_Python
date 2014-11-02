# Unique Binary Search Trees 
class Solution:
    # @return an integer
    def numTrees(n):
        # DP
        mp = {0: 1, 1: 1} # key: n, value: number of different structures
        if n in mp:
        	return mp[n]
    
        for i in range(2, n+1):  # i nodes
        	res = 0
        	sm = 0
        	for j in range(0, i):# j nodes can be put either on the left or on the right. j in [0,i-1]
        	    sm += mp[j] * mp[i-1-j]
        	res += sm
        	mp[i] = res
        return mp[n]

        # recursive method
        # if n == 0 or n == 1:
        #     return 1
        # res = 0
        # for i in xrange(0, n):
        #     # assign i nodes on the left and (n-1-i) on the right
        #     # because left side is independent of right side, so multiply them
        #     res += self.numTrees(i) * self.numTrees(n - 1 -i)
        # return res