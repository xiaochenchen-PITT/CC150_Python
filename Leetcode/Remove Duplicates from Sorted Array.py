class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                A.pop(i)
                continue
            i += 1
        return len(A)

    def removeDuplicates2(self, A):
        # if del(), pop(), remove() are not allowed!
        if len(A) == 0 or len(A) == 1:
            return len(A)
        count = 1
        for i in xrange(1, len(A)):
            if A[i-1] != A[i]:
                A[count] = A[i]
                count += 1
        return count

s = Solution()
A = [1,1,1,2,2,3,3,3,3]
print s.removeDuplicates(A)
print s.removeDuplicates2(A)