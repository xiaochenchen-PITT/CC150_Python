class Solution:
    # @param A, a sorted list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        i = 0
        # if found
        for node in A:
            if node == target:
                return i
            i += 1
        # if not found
        if target < A[0]:
            return 0
        for i in range(1, len(A)):
            if target > A[i-1] and target < A[i]:
                return i
        return len(A)