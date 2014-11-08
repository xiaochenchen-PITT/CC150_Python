class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        '''because it is possible for num[mid] == num[left] and num[mid] == num[right] to happen,
        move towards left and right at one step together. Thus affects the time complexit to worst case O(N)'''
        # [2,2,2,2,2,2,2,2,2,2,2,1,2,2,2] [2,1,2,2,2,2,2,2,2,2]
        # [1,2,3,4,5,6,7]
        # [6,7,1,2,3,4,5]
        # [3,4,5,6,7,1,2]
        left = 0
        right = len(num) - 1
        while right - left >= 2:
            mid = left + ((right - left) / 2)
            if num[mid] == num[left] and num[mid] == num[right]: # in this case, both num[left] and num[right] are not
                left += 1                                       # the minimum, discard them both
                right -= 1
            else:
                if num[left] <= num[mid] and num[mid] <= num[right]:
                    return num[left]
                if num[left] > num[mid]:
                    right = mid
                elif num[mid] > num[right]:
                    left = mid
        return num[left] if num[left] < num[right] else num[right]