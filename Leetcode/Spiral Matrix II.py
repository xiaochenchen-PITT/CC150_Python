class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        mat = []
        for i in range(0, n):
            mat.append([0]*n)
        row, col = 0, 0
        dire = 'right'
        for i in range(1, (n*n)+1):
            if dire == 'right':
                mat[row][col] = i
                col += 1
                if col == n or mat[row][col] != 0:
                    col -= 1
                    row += 1
                    dire = 'down'
            elif dire == 'down':
                mat[row][col] = i
                row += 1
                if row == n or mat[row][col] != 0:
                    row -= 1
                    col -= 1
                    dire = 'left'
            elif dire == 'left':
                mat[row][col] = i
                col -= 1
                if col == -1 or mat[row][col] != 0:
                    col += 1
                    row -= 1
                    dire = 'up'
            else: # up
                mat[row][col] = i
                row -= 1
                if mat[row][col] != 0:
                    row += 1
                    col += 1
                    dire = 'right'
        return mat