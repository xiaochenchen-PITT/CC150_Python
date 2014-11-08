class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.res = []
        self.DFS(n, k, [])
        return self.res
        
    def DFS(self, n, k, comb):
        if len(comb) == k:
            if comb not in self.res:
                self.res.append(comb)
            return
        for i in range(1, n+1):
            if i not in comb: # make sure no duplicate in the result
                if not comb or i > comb[-1]: # make sure it is in ascending order
                    self.DFS(n, k, comb + [i])
        
s = Solution()
print s.combine(10, 7)