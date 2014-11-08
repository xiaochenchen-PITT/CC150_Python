class Solution:
    # @return a list of integers
    def getRow(self, rowIndex, pas = [1]):
        '''hint: only O(N) extra space, meaning storing from 0th to nth lists is not allowed.'''
        if len(pas)-1 == rowIndex:
            return pas
        next_pas = [1]
        for i in range(0, len(pas)):
            if i == len(pas)-1:
                next_pas.append(1)
            else:
                next_pas.append(pas[i+1]+pas[i])
        return self.getRow(rowIndex, next_pas)
