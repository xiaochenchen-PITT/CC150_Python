class Solution:
    # @return an integer
    def uniquePaths1(self, m, n):
        # brute force DFS
        if m == 1 or n == 1:
            return 1
        self.count = 0
        self.DFS(m, n, 1, 1)
        return self.count
        
    def DFS(self, m, n, loc_x, loc_y):
        # print loc_x, loc_y
        if loc_x == n and loc_y == m:
            self.count += 1
            return
        if loc_x > n or loc_y > m:
            return
        for i in [0, 1]:
            self.DFS(m, n, loc_x + 1 - i, loc_y + i)

    def uniquePaths(self, m, n):
        # DP
        # Chessboard question: always build a list of lists to mimic 
        #                     Chessboard, either for checking state or DP
        cols = [0]*n
        rows = []
        for i in xrange(0, m):
            rows.append(cols)
        for row in range(0, m):
            for col in range(0, n):
                if row == 0 or col == 0: # edges
                    rows[row][col] = 1
                else:
                    rows[row][col] = rows[row-1][col] + rows[row][col-1]
        return rows[m-1][n-1]

s = Solution()
print s.uniquePaths(6,13)
print s.uniquePaths1(6,13)
