class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        '''hint: just inplace quick sort'''
        if len(A) <= 1:
            return A
        return self.qsort(A, 0, len(A)-1)

    def qsort(self, A, left, right):
        if left < right:
            new_pivot = self.partition(A, left, right)
            self.qsort(A, left, new_pivot-1)
            self.qsort(A, new_pivot+1, right)
            return A

    def partition(self, A, left, right):
        pivot = A[right]
        for i in range(left, right):
            if A[i] < pivot:
                A[i], A[left] = A[left], A[i]
                left += 1
        A[right], A[left] = A[left], A[right]
        return left

s = Solution()
print s.sortColors([1,0,1,2,0,1,2,0,0,2,2,1])