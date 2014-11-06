class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        '''hint: build a list of lists to solve this chessboard / grid question.'''
        m = len(grid)
        n = len(grid[0])
        l = [0]*n
        chessboard = []
        for i in range(0, m):
            chessboard.append(l)
        chessboard[0][0] = 1
        for row in range(0, m):
            for col in range(0, n):
                if row == 0 and col == 0:
                    chessboard[0][0] = grid[0][0]
                elif row == 0:
                    chessboard[row][col] = chessboard[row][col-1] + grid[row][col] 
                elif col == 0:
                    chessboard[row][col] = chessboard[row-1][col] + grid[row][col] 
                else:
                    chessboard[row][col] = min(chessboard[row-1][col], chessboard[row][col-1]) + grid[row][col]
        return chessboard[-1][-1]