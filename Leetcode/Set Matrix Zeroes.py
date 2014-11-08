class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.

    # def setZeroes(self, matrix):
    #     # using extra space
    #     zeros = []
    #     for row in range(0, len(matrix)):
    #         for col in range(0, len(matrix[0])):
    #             if matrix[row][col] == 0:
    #                 zeros.append([row, col])
    #     for loc in zeros:
    #         for col in range(0, len(matrix[0])):
    #             matrix[loc[0]][col] = 0
    #         for row in range(0, len(matrix)):
    #             matrix[row][loc[1]] = 0
    #     return matrix

    def setZeroes(self, matrix):
        # not using extra space
        # hint: when constant space is required, there are normally 2 ways:
        #         1. use one or two variables
        #         2. use the problem space itself to store the needed information

        isFirstRowHasZero, isFirstColHasZero = False, False
        # 1. decide if the first row and first col has 0 and has to be zeroed out later
        # use two variables to store this information
        for row in range(0, len(matrix)):
            if matrix[row][0] == 0:
                isFirstColHasZero = True
        for col in range(0, len(matrix[0])):
            if matrix[0][col] == 0:
                isFirstRowHasZero = True
        print isFirstColHasZero, isFirstRowHasZero
        # 2. for [1..n], save the zero-out flag in the first row and col respectivey
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        # 3. use the information stored in the first row and col to set zero
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for c in range(1, len(matrix[0])):
                    matrix[row][c] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][col] = 0
        # 4. use the two variables to set the first row and col 
        if isFirstColHasZero:
            for row in range(0, len(matrix)):
                matrix[row][0] = 0
        if isFirstRowHasZero:
            for col in range(0, len(matrix[0])):
                matrix[0][col] = 0

        return matrix

s = Solution()
mat = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print s.setZeroes(mat)
                    