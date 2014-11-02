class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        # Non-DP approach:
        # O(N) = 1.618 ^ n
        # if n == 1 or n == 2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # DP approach: 
        # 1. Find a recursive solution that involves repeated computations
        # 2. Save the result of each time in the BOTTOM-UP method to avoid 
        #    recalculation
        mp = {1:1, 2:2}
        if n in mp:
            return mp[n]
        for i in xrange(3, n+1):
            mp[i] = mp[i-2] + mp[i-1]
        return mp[n]

s = Solution()
print s.climbStairs(300)