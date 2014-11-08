class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort() # does not hurt to sort, it is not the bottleneck anyway...
        self.res = []
        self.DFS(S, [])
        return self.res
        
    def DFS(self, S, subset):
        if subset not in self.res:
            self.res.append(subset)
        for num in S:
            if num not in subset: # make sure no duplicate in the res
                if not subset or num > subset[-1]: # always pass through the next element 
                    self.DFS(S, subset + [num])
        
        