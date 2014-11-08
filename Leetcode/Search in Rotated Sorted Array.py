class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1
        while right >= left:
            if A[left] == target:
                return left
            if A[right] == target:
                return right
            mid = left + (right-left) / 2
            if A[mid] == target:
                return mid

            if A[left] < A[mid]: # left sorted
                if target > A[left] and target < A[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else: # right sorted
                if target > A[mid] and target < A[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1