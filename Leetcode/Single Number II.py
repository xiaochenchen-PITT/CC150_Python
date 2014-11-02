class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        '''time: O(N), space: O(1)'''
        ones = 0  # ones[i] stands for how many ith bit of all numbers showed up once
        twos = 0  # twos[i] stands for how many ith bit of all numbers showed up twice
        threes = 0# threes[i] stands for how many ith bit of all numbers showed up three times
        for i in range(0, len(A)):
        	twos |= A[i] & ones
        	ones ^= A[i]
        	threes = ones & twos
        	ones &= ~threes
        	twos &= ~threes
        return ones

s = Solution()
print s.singleNumber([2,2,3,2])
