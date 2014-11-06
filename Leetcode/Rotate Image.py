class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        '''hint: reverse the matrix first, 
        then interchange elements along the diagonal'''
        matrix = matrix[::-1]
        for row in range(0, len(matrix)):
            for col in range(row, len(matrix)):
                t = matrix[col][row]
                matrix[col][row] = matrix[row][col]
                matrix[row][col] = t
        return matrix
