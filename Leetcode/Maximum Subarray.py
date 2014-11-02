class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        '''hint: whether you should add the next element or drop off the subarry 
                and start a new one'''
        currmax = A[0]
        max = A[0]
        for i in range(1, len(A)):
            if currmax > 0:
                currmax += A[i]
            else:
                currmax = A[i]
                    
            if currmax > max:
                max = currmax
        return max