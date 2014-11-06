class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        '''hint: binary search, remember to include A[mid] when slice'''
        if len(num) == 0:
            return
        if len(num) == 1:
            return num[0]
        if len(num) == 2:
            return num[0] if num[0] < num[1] else num[1] 
            
        mid = 0 + (len(num) - 1) / 2
        if num[0] > num[mid]:
            new_num = num[:mid+1]
        elif num[mid] > num[-1]:
            new_num = num[mid:]
        else:
            return num[0]
        return self.findMin(new_num)