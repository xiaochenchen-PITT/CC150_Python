class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        '''hint: for each position, the volume is determined by:
            min(its highest points on left and on right)'''
        if not A or len(A) < 3:
            return 0
        left_max, right_max = [], [] # left_max and 
        vol = 0
        height_max = 0
        for left in range(0, len(A)):
            if A[left] > height_max:
                height_max = A[left]
            left_max.append(height_max)
        height_max = 0
        for right in range(0, len(A)):
            if A[len(A)-1-right] > height_max:
                height_max = A[len(A)-1-right]
            right_max.append(height_max)
        right_max = right_max[::-1]
        for i in range(0, len(A)):
            vol += min(right_max[i], left_max[i]) - A[i]
        return vol