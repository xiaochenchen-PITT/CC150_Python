class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) < 3:
            return True if target in A else False
        mid = (len(A)-1) / 2
        if A[0] < A[mid]: # left sorted
            if target >= A[0] and target < A[mid]:
                new_A = A[:mid+1]
            else:
                new_A = A[mid:]
        else: # right sorted
            if target > A[mid] and target <= A[-1]:
                new_A = A[mid:]
            else:
                new_A = A[:mid+1]
        return self.search(new_A, target)

s = Solution()
print s.search([1,3,5], 2)