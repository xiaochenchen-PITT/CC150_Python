'''N-Queens question, typical NP question, give up the time complexity constraints.
The time complexity is definitely going to be exponential'''
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        '''hint: use several array to check the validity of placing a queen in the chessboard'''
    	self.count = 0
    	self.DFS(n)
    	return self.count

    def DFS(self, n, state = [], state_rmc = [], state_rpc = [], row = 0):
        '''state : index is the row, state[index] is col, used for checking row and col collision.
            state_rmc : row-col, used for checking one diagonal(upper right to lower left)
            state_rpc : row+col, used for checking the other diagonal(upper left to lower right)'''
        if row == n:
            self.count += 1
        for col in range(0, n):
            if col not in state and (row+col) not in state_rpc and (row-col) not in state_rmc:
                self.DFS(n, state + [col], state_rmc + [row-col], state_rpc + [row+col], row + 1)
        return self.count  	


s = Solution()
print s.totalNQueens(8)