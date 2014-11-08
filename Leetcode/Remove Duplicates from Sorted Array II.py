class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        i = 1
        while i < len(A):
            if A[i] == A[i-1]:
                i += 1
                while i < len(A) and A[i] == A[i-1]:
                    A.pop(i)
                else:
                    i += 1
            else:
                i += 1
        return len(A)