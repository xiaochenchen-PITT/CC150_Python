class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        n = len(num)
        self.res = []
        self.DFS(num, n, [])
        return self.res
        
    def DFS(self, num, n, permutation):
        if len(permutation) == n:
            self.res.append(permutation)
            return 
        for i in num:
            if i not in permutation:
                self.DFS(num, n, permutation + [i])
        
        