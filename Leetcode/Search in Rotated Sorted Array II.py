class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        '''hint: it is really important to dicide to go left or right for this question, only 
        go left if A[0] < A[mid] or 
        go right if A[0] > A[mid]'''
        if len(A) == 1 or len(A) == 2:
            return True if target in A else False
        mid = (len(A)-1) / 2
        if A[mid] == target:
            return True
            
        if A[0] < A[mid]: # left sorted 
            if target >= A[0] and target < A[mid]:
                new_A = A[:mid+1]
            else:
                new_A = A[mid:]
        else:  
            if A[0] > A[mid]: # right sorted
                if target > A[mid] and target <= A[-1]:
                    new_A = A[mid:]
                else:
                    new_A = A[:mid+1]
            else:
                new_A = A[1:]
        return self.search(new_A,target)
        
        
        