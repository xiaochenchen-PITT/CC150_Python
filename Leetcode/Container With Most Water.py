class Solution:
    # @return an integer
    # def maxArea(self, l):
    #     max_vol = 0
    #     beginning = 0
    #     ending = 0
    #     for i in range(0, len(l)):
    #         for j in range(i, len(l)):
    #             if (j - i) * min(l[i], l[j]) > max_vol:
    #                 max_vol = (j - i) * min(l[i], l[j])
    #                 beginning = i
    #                 ending = j
    #     return max_vol

    def maxArea(self, height):
        # Two pointers
        left = 0
        right = len(height) - 1
        max_vol = 0
        while right > left:
            max_vol = max(max_vol, (right-left)*min(height[left], height[right]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_vol
            
s = Solution()
A = [7,6,5,4,3,2,1]
print s.maxArea(A)